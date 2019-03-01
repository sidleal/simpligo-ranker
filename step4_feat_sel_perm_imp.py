import numpy
import pandas

from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split

from keras.models import Sequential
from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
import pickle
import math
import eli5
from eli5.sklearn import PermutationImportance


input_size = 189
pipeline = None


def baseline_model():
    model = Sequential()
    model.add(Dense(30, input_dim=input_size, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation="relu"))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

estimators = []
with open('models/pss2_regressor_std_scaler_all.pickle', 'rb') as handle:
    std_scaler = pickle.load(handle)
    estimators.append(('standardize', std_scaler))

estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=10, verbose=1)
estimator.model = load_model("models/model_pss2_regressor_all.h5")

estimators.append(('mlp', estimator))
pipeline = Pipeline(estimators)


# load dataset
pandas.set_option('display.max_colwidth', -1)
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
Y = numpy.asanyarray(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)


perm = PermutationImportance(pipeline, random_state=1)

res = perm.fit(X_test,y_test)

#ret = eli5.format_as_text(eli5.explain_weights(perm))
ret = eli5.format_as_dict(eli5.explain_weights(res))

#ret = eli5.show_weights(perm, feature_names = X.columns.tolist())
print(ret)

for i in ret['feature_importances']['importances']:
    print(i)

print('------')
print(perm.feature_importances_)
