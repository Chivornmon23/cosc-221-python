import numpy as np

#scalar arithmetic
# array = np.array([1, 2, 3])
# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 2)
# print(np.sqrt(array))

# print(np.round(array))
# print(np.floor(array))
# print(np.ceil(array))
# print(np.pi)

#vectorized math funcs
# radii = np.array([1, 2, 3])
# print(np.pi * radii ** 2)

# Elemet-wise arithmetic
# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
#
# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 ** array2)

# Comparision operators
scores = np.array([91, 55, 100, 73, 82, 64])
# print(scores < 50)
scores[scores < 60] = 0
print(scores)