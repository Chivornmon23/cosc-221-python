import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

print(f"Dimension: {array.ndim}")
print(f"Shape: {array.shape}")
print(f"Chain indexing: {array[0][1][2]}")
print(f"Multidimensional indexing: {array[1, 1, 1]}")
print(f"Multidimensional indexing: {array[0, 2, 2]}")
print(f"Multidimensional indexing: {array[0, 2, 0]}")
print(f"Multidimensional indexing: {array[0, 2, 0]}")
print(f"Multidimensional indexing: {array[0, 1, 1]}")
print(f"Multidimensional indexing: {array[1, 2, 2]}")

word = array[1, 1, 1] + array[0, 2, 2] + array[0, 2, 0] + array[0, 2, 0] + array[0, 1, 1] + array[1, 2, 2]
print(f"Hello, {word}!")
