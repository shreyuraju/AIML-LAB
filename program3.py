import pandas as pd

dataset = pd.read_csv('./enjoysports.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

POSITIVE = 'yes'

specificH = X[0].copy()
generalH = [['?' for i in range(len(X[0]))] for j in range(len(X[0]))]

for i, row in enumerate(X):
    if y[i] == POSITIVE:
        for j, item in enumerate(row):
            if specificH[j] != item:
                specificH[j] = '?'

    else:
        for j, item in enumerate(row):
            if specificH[j] != item:
                generalH[j][j] = specificH[j]

for i, row in enumerate(generalH):
    for j, item in enumerate(row):
        if item not in specificH:
            generalH[i][j] = '?'

for i in range(generalH.count(['?' for i in range(len(X[0]))])):
    generalH.remove(['?' for i in range(len(X[0]))])

print(specificH)
print(generalH)
