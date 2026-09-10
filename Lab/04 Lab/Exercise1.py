# Exercise 1: Exponential function 

# def expo (x, n): 
#     if n == 0: 
#         return 1
#     return x * expo(x, n-1)

# ns = [10, 100, 200, 300]

# for n in ns: 
#     val1 = expo(3.14159, n)
#     val2 = expo(3.14, n)
#     diff = val1 - val2
#     print(f"n = {n}: {diff}")

import time

# 1. Recursive power function
def expo(x, n):
    if n == 0: 
        return 1.0
    return x * expo(x,n-1)
# 2. Recursive factorial function
def factorial(n):
    if n == 0 or n ==1: 
        return 1.0
    return n * factorial(n-1)

# 3. Recursive exp(x, n) function (summing n terms)
def exp(x, n):
    if n == 0:
        return 1.0  # The first term is always 1 (x^0 / 0!)
    # Add current term to the sum of the previous terms
    term = expo(x, n) / factorial(n)
    return term + exp(x, n - 1)

# Testing Task 1: Estimate e using exp(1, n)
for n in [10, 100, 500]:
    start_time = time.time()
    result = exp(1, n)
    end_time = time.time()
    print(f"n = {n}: result = {result}, time = {end_time - start_time:.6f} seconds")

