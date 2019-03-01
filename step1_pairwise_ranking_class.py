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


input_size = 378 #189*2

# define base model
def baseline_model():
    model = Sequential()
    model.add(Dense(30, input_dim=input_size, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation="sigmoid"))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

pandas.set_option('display.max_colwidth', -1)

# load dataset
df = pandas.read_csv("data/pss2_features_pairs_align.tsv", delimiter='\t', header=0)

X = pandas.concat([df.iloc[:, 5:194], df.iloc[:, 195:384]], axis=1)
Y = df.iloc[:, 3]

acertos = 0
erros = 0
for idx, row in X.iterrows():
    if row['fr_flesch'] < row['to_flesch'] and Y[idx] == 0:
        acertos+=1
    else:
        erros+=1

print("FLESCH - Acertos: %s - Erros: %s - Total: %s - Acurácia: %02.2f" % (acertos, erros, erros + acertos, acertos * 100 / (erros+acertos)))

acertos = 0
erros = 0
for idx, row in X.iterrows():
    if row['fr_gunning_fox'] > row['to_gunning_fox'] and Y[idx] == 0:
        acertos+=1
    else:
        erros+=1

print("GUNNING FOX - Acertos: %s - Erros: %s - Total: %s - Acurácia: %02.2f" % (acertos, erros, erros + acertos, acertos * 100 / (erros+acertos)))

estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=10, verbose=0)

estimators = []
standardScaler = StandardScaler()
estimators.append(('standardize', standardScaler))
estimators.append(('mlp', estimator))
pipeline = Pipeline(estimators)

total_acuracia = 0
total_fscore = 0

for z in range (0, 10): #10-fold
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)

    pipeline.fit(X_train, y_train)

    prediction = pipeline.predict(X_test)

    y_test = numpy.asanyarray(y_test)

    for j in range(0, len(prediction)):
        #print("%s - %s" % (y_test[j], prediction[j]))
        if prediction[j] > 0.5:
            prediction[j] = 1
        else:
            prediction[j] = 0

    print(accuracy_score(y_test, prediction))

    truePos = 0
    trueNeg = 0
    falsePos = 0
    falseNeg = 0
    for j in range(0, len(prediction)):
        if y_test[j] == 1 and prediction[j] == 1:
            truePos+=1
        if y_test[j] == 0 and prediction[j] == 0:
            trueNeg+=1
        if y_test[j] == 1 and prediction[j] == 0:
            falseNeg+=1
        if y_test[j] == 0 and prediction[j] == 1:
            falsePos+=1

    acuracia = (truePos + trueNeg) / (truePos+trueNeg+falsePos+falseNeg)
    print("acuracia %s" % acuracia)
    total_acuracia += acuracia

    recall = truePos / (truePos+falseNeg)
    precision = truePos / (truePos+falsePos)

    fscore = (2 * (precision * recall)) / (precision + recall)

    print("---------------")
    print("recall %s" % recall)
    print("precision %s" % precision)
    print("fscore %s" %fscore)
    total_fscore+= fscore
    print("---------------")

print("=================")
print("total acuracia %s" % (total_acuracia/10))
print("total fscore %s" % (total_fscore/10))
print("=================")

#salva o modelo
with open('models/pss2_std_scaler_class.pickle', 'wb') as handle:
    pickle.dump(standardScaler, handle, protocol=pickle.HIGHEST_PROTOCOL)

estimator.model.save("models/model_pss2_class.h5")
print("Saved model to disk")

