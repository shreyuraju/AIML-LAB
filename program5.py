import numpy as np
import pandas as pd

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

X = X / np.amax(X, axis=0)
y = y / 100

inputLN = 2
hiddenLN = 3
outputLN = 1

epochs = 999999
lr = 0.1

hiddenLW = np.random.uniform(size=(inputLN, hiddenLN))
outputLW = np.random.uniform(size=(hiddenLN, outputLN))
hiddenLB = np.random.uniform(size=(1, hiddenLN))
outputLB = np.random.uniform(size=(1, outputLN))


def sigmoid(n):
    return 1 / (1 + np.exp(-n))


def derivativeSigmoid(n):
    return n * (1 - n)


for i in range(epochs):
    hiddenLOut = np.dot(X, hiddenLW) + hiddenLB
    hiddenLAct = sigmoid(hiddenLOut)

    outputLOut = np.dot(hiddenLAct, outputLW) + outputLB
    outputLAct = sigmoid(outputLOut)

    outputGrad = derivativeSigmoid(outputLAct)
    hiddenGrad = derivativeSigmoid(hiddenLAct)

    EO = y - outputLAct
    d_output = EO * outputGrad

    EH = d_output.dot(outputLW.T)
    d_hidden = EH * hiddenGrad

    outputLW += hiddenLAct.T.dot(d_output) * lr
    hiddenLW += X.T.dot(d_hidden) + lr

print(X)
print(y)
print(outputLAct)
