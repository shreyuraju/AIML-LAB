import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X / np.amax(X, axis=0)
y = y / 100

inputLayers = 2
hiddenLayers = 3
outputLayers = 1

hW = np.random.uniform(size=(inputLayers, hiddenLayers))
oW = np.random.uniform(size=(hiddenLayers, outputLayers))
hB = np.random.uniform(size=(1, hiddenLayers))
oB = np.random.uniform(size=(1, outputLayers))
epochs = 999999
lr = 0.01

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def derivativeSignmoid(x):
    return x*(1-x)

for i in range(epochs):
    hiddenLInput = np.dot(X, hW) + hB
    hiddenLOutput = sigmoid(hiddenLInput)
    
    outputLInput = np.dot(hiddenLOutput, oW) + oB
    outputLOutput = sigmoid(outputLInput)
    
    outputGrad = derivativeSignmoid(outputLOutput)
    hiddenGrad = derivativeSignmoid(hiddenLOutput)
    
    EO = y - outputLOutput
    d_output = EO * outputGrad
    
    EH = d_output.dot(oW.T)
    d_hidden = EH * hiddenGrad
    
    oW += hiddenLOutput.T.dot(d_output) * lr
    hW += X.T.dot(d_hidden) * lr
    
    print(y)
    print(outputLOutput)