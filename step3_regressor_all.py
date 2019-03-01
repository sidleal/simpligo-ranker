import numpy
import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split

from keras.models import Sequential
from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
import pickle
import math

input_size = 189

# define base model
def baseline_model():
    model = Sequential()
    model.add(Dense(30, input_dim=input_size, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation='relu'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

pandas.set_option('display.max_colwidth', -1)

# load dataset
df = pandas.read_csv("data/pss2_ranking_global.tsv", delimiter='\t', header=0)

X = df.iloc[:, 3:194]
Y_tmp = df.iloc[:, 0]
Y = []

total_sents = len(Y_tmp)
for i in range(0,total_sents):
    Y.append(Y_tmp[i]/total_sents)

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=10, verbose=1)

estimators = []
standardScaler = StandardScaler()
estimators.append(('standardize', standardScaler))
estimators.append(('mlp', estimator))
pipeline = Pipeline(estimators)

Y = numpy.asanyarray(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

pipeline.fit(X_train, y_train)
prediction = pipeline.predict(X_test)

y_test = numpy.asanyarray(y_test)

error = 0
for j in range(0, len(prediction)):
    print("%s - %s" % (y_test[j], prediction[j]))
    error = error + (prediction[j] - y_test[j])**2

print("MEAN SQUARED ERROR:", error/len(prediction))

with open('models/pss2_regressor_std_scaler_all.pickle', 'wb') as handle:
    pickle.dump(standardScaler, handle, protocol=pickle.HIGHEST_PROTOCOL)

estimator.model.save("models/model_pss2_regressor_all.h5")
print("Saved model to disk")

