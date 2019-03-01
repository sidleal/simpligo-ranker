import numpy
import pickle

from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.pipeline import Pipeline

input_size = 189
pipeline = None

def baseline_model():
    model = Sequential()
    model.add(Dense(30, input_dim=input_size, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation="relu"))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

estimators = []
with open('models/pss2_regressor_std_scaler_50.pickle', 'rb') as handle:
    std_scaler = pickle.load(handle)
    estimators.append(('standardize', std_scaler))

estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=10, verbose=1)
estimator.model = load_model("models/model_pss2_regressor_50.h5")

estimators.append(('mlp', estimator))
pipeline = Pipeline(estimators)

#Só é possível votar em 20 candidatos, já que as Pirâmides de Gizé, por serem o último remanescente das Sete Maravilhas da Antigüidade e devido a protestos do governo egípcio, foram consideradas um candidato honorário e estão fora da competição -- seriam a oitava maravilha.
input = numpy.array([0.1136,0.0227,0.6136,8.0568,0.3864,1.0,3.037,44.0,0.3182,1.0,1.0,44.0,0.0,0.1591,0.0455,0.0455,0.0,0.0,0.0,1860570.7037,45.0,0.2857,7.7719,2246.052,0.0,0.9318,0.0909,0.0,0.0455,0.0,0.0227,0.0,0.0227,0.0,0.0227,1.2,0.0,2.0,12.0,3.7755,9.5,111.0,1.5882,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,6.0,1.0,0.5,6.0,0.0,1.0,0.3333,0.6667,0.0,0.0,0.0,0.2857,0.5714,0.4286,0.1429,0.1667,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.6296,0.3333,0.0,0.0,1.0,0.1136,0.1136,0.0,1.0,0.0,0.0,0.0,3.9717,0.6639,0.0,0.5,0.5,0.0,1.0,0.551,0.551,0.0,4.5455,11.5607,4.0,0.0682,4.6914,0.8829,0.0,0.2222,0.4444,0.3333,0.8824,17.7636,0.0455,4.8879,1.5654,0.0556,0.3333,0.2778,0.2222,4.2476,0.6195,0.0,0.4444,0.5556,0.0,0.0,0.0,14.0,5.3333,0.0,2.0,0.05,0.05,1.0,0.3182,0.3182,0.0,0.0,0.6667,1.0,0.0,0.0,0.0,0.0,0.0,0.6667,0.1633,0.0227,0.5,0.0,0.0,0.2,0.0,0.0,0.2,0.4,0.2,0.3333,0.0,0.0,0.0,0.0,0.5,0.0,0.0,0.0,0.6667,0.0,44.0,44.0,0.0,0.0,4.0277,1.0,0.1364,0.1364,0.0,1.0,0.6296])
input = input.reshape(1, -1)
prediction = pipeline.predict(input)
print(prediction)