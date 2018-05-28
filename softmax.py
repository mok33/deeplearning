"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
	return np.exp(x) / sum(np.exp(x))



#print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = scores = np.array([[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]])

print(softmax(x))
