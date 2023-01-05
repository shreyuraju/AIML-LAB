import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import classification_report as cr, confusion_matrix as cm, accuracy_score as acs
from sklearn.neighbors import KNeighborsClassifier

dataset = datasets.load_iris()
X = dataset.data
y = dataset.target

X_train, X_test, y_train, y_test = tts(X, y, test_size=0.1, random_state=0)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

[print(f'Label {index} - {item}') for index, item in enumerate(dataset.target_names)]

y_pred = classifier.predict(X_test)
print(np.concatenate((y_test.reshape(len(y_test),1), y_pred.reshape(len(y_pred),1)),1))

print(f'Accuracy: {acs(y_test, y_pred)*100}%')
print(f'Classification Report:\n{cr(y_test, y_pred)}')
print(f'Confusion Matrix\n{cm(y_test, y_pred)}')