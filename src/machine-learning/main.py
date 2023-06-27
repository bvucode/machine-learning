from neuralnetwork import NeuralNetwork
from activation import Activation

weights = [[0.1, 0.1, -0.3], # травмы?
           [0.1, 0.2, 0.0],  # победа?
           [0.0, 1.3, 0.1]]  # печаль?

input = [8.5, 0.65, 1.2]

true = [0.1, 1, 0.1]

alpha = 0.01

error = [0, 0, 0]
delta = [0, 0, 0]

pred = NeuralNetwork(input, weights)
lpred = pred.neuralnetwork()

def fnerror(pred, true):
    error = [0, 0, 0]
    for i in range(len(true)):
        error[i] = (pred[i] - true[i]) ** 2
    return error

def fndelta(pred, true):
    delta = [0, 0, 0]
    for i in range(len(true)):
        delta[i] = pred[i] - true[i]
    return delta

error = fnerror(lpred, true)

delta = fndelta(lpred, true)

Activation.ele_mul(lpred, true, input, weights, alpha)

print("prediction: ", lpred, "error: ", error, "delta: ", delta)
print("weights after correction: ", weights)
