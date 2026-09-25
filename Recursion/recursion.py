# Recursion 

# exponential 
def expo(x, n):
    if n == 0:
        return 1
    return x * expo(x, n-1)

# factorial 
def factorial (n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
    
# using for loop to compute factorial number 
def factorial_using_loop(n):
    result = 1
    for i in range (1, n+1):
        result = result * i
    return result 
# Challenge2
def compute_sn(n):
    # Base case: if n is 1, return 1.0
    if n == 1:
        return 1.0
    
    # Recursive step: S_n = S_{n-1} + current term
    # (-1)**(n - 1) handles the alternating positive and negative signs
    current_term = ((-1) ** (n - 1)) / n
    return compute_sn(n - 1) + current_term

# Compute for values: 10, 100, 200, 300
for n_val in [10, 100, 200, 300]:
    print(f"S_{n_val} = {compute_sn(n_val):.4f}")

# Fibonacci numbers
def rabbit_population(n):
    # Base cases: for month 1 or 2, population is 1
    if n == 1 or n == 2:
        return 1
    # Recursive step: F_n = F_{n-1} + F_{n-2}
    return rabbit_population(n - 1) + rabbit_population(n - 2)

# Palindrome Problem 
# A string is a palindrome if it reads the same from the left and from the right 

# Challenge: Write a recursive function isPalindrome(s) to check if a string s is palindrome
#           or not

# def isPalindrome(s): 
#     if len(s) <= 1: # Base case
#         return True
#     elif s[0] != s[len(s) - 1]: #Base case
#         return False
#     else: 
#         return isPalindrome(s[1: len(s) -1])

# word = "ROTATOR"
# print(f"The word {word} is a palindrome?: {isPalindrome(word)}")

def isPalindrome(s): 
    return isPalindromeHelper(s, 0, len(s)-1)
def isPalindromeHelper(s, low, high):
    if high <= low: #Base case
        return True
    elif s[low] != s[high]: #Base case
        return False
    else: 
        return isPalindromeHelper(s, low + 1, high - 1)
    
