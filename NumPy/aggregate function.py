import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Maximum: ", np.max(arr))
print("Minimum: ", np.min(arr))

two_d_arr = np.array([[1, 2, 3],
                      [4, 5, 6]])

print(np.sum(two_d_arr, axis=0))
print(np.sum(two_d_arr, axis=1))