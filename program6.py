import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts

dataset = pd.read_csv('./id3.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)
print(y)

X_train, X_test, y_train, y_test = tts(X, y, test_size=0.4, random_state=0)

print(X_train, y_train)

print(X_test, y_test)

pYes = list(y_train).count('yes')/y_train.size
pNo = list(y_train).count('no')/y_train.size
print(pYes)
print(pNo)

pYesValues = {}
pNoValues = {}
valuesYes = {}
valuesNo = {}

for i, row in enumerate(X_train):
    for j, vals in enumerate(row):
        if y_train[i] == 'yes':
            valuesYes[vals] = valuesYes.get(vals, 0) + 1
        elif y_train[i] == 'no':
            valuesNo[vals] = valuesNo.get(vals, 0) + 1
print(valuesYes, '\n', valuesNo)

uniqueValues = set(list(valuesYes.keys())+list(valuesNo.keys()))
print(uniqueValues)
for val in uniqueValues:
    pYesValues[val] = valuesYes.get(val, 0)/list(y_train).count('yes')
    pNoValues[val] = valuesNo.get(val, 0)/list(y_train).count('no')
print(pYesValues, '\n', pNoValues)

y_pred = []
data = []
header = ['Test Instance', 'Predicted Output', 'Actual Output']
print('predicting the test set...')
print('Test\t\t\t\t\tPrediction\tActual Output')
for i, row in enumerate(X_test):
    pYesInstance = pYes
    pNoInstance = pNo
    for j, val in enumerate(row):
        pYesInstance *= pYesValues.get(val, 0)
        pNoInstance *= pNoValues.get(val, 0)
    pYesInstanceNormalized = pYesInstance/((pYesInstance + pNoInstance) or 1)
    pNoInstanceNormalized = pNoInstance/((pYesInstance + pNoInstance) or 1)
    y_pred.append('yes' if pYesInstanceNormalized >= pNoInstanceNormalized else 'no')
    print(row, '\t', y_pred[i], '\t\t', y_test[i])
    #print(f'{row}\t{y_pred[i]}\t\t{y_test[i]}')
    
from sklearn.metrics import accuracy_score as acs
print('accuracy is ', acs(y_test, y_pred)*100)

print((0+5) or 1)