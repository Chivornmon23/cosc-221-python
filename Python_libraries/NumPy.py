import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([60, 70, 80, 90])

print(scores)
print(scores.shape)
print(scores.ndim)

scores = np.array([60, 70, 80, 90] + [100])
print(scores)

scores = np.array([60, 70] * 2)
print(scores)

scores = np.array([60, 70, 80, 90])
adjusted = scores + 5

print(adjusted)
print(scores)

matrix = scores.reshape(2, 2)
print(matrix)
print(matrix.shape)

print(scores.mean())
print(scores.min())
print(scores.max())