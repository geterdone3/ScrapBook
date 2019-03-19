#!/usr/bin/env python3

import numpy as np
# from math import exp
# from random import random


def sigmoid(x):
  return 1.0/(1 + np.exp(-x))


def sigmoid_derivative(x):
  return x * (1.0 - x)


class NeuralNetwork:
  def __init__(self, inputs, answers, layers):
    self.inputs  = inputs
    self.answers = answers
    self.layers  = np.array([len(inputs[0])] + layers.tolist() + [1])

    # 3d array mapping each layer's nodes to the next layer's nodes
    self.weights_1 = np.array([np.random.rand(self.layers[l], self.layers[l+1]) for l in range(len(self.layers)-1)])
    self.weights_2 = self.weights_1.copy()

  def feedforward(self, inputs):
    for l in range(len(self.weights_1)):
      self.weights_2[l] = sigmoid(np.dot(inputs, self.weights_1[l]))
      inputs = self.weights_2[l]
    return inputs

  def backprop(self):
    # application of the chain rule to find derivative of the loss function with respect to each layer
    output = self.weights_2[-1].copy()
  
    for l in range(len(self.weights_1)-1, 0, -1):
      self.weights_2[l] = np.dot(self.weights_2[l-1].T, (2*(self.answers - self.weights_2[l]) * sigmoid_derivative(self.weights_2[l])))
    self.weights_2[0] = np.dot(self.inputs.T, (np.dot(2*(self.answers - self.weights_1[1]) * sigmoid_derivative(self.weights_1[1]), self.weights_1[1].T) * sigmoid_derivative(self.weights_2[1])))

    # update the weights with the derivative (slope) of the loss function
    self.weights_1 += self.weights_2
    self.weights_2 = self.weights_1.copy()

  def train(self, interations):
    for i in range(interations):
      self.feedforward(self.inputs)
      self.backprop()


if __name__ == "__main__":
  inputs  = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
  answers = np.array([[0], [1], [1], [0]])
  layers = np.array([4])

  n = NeuralNetwork(inputs, answers, layers)
  n.train(1500)

  print(n.feedforward(inputs))
