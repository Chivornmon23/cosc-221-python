def isPalindromeNum(n): 
    digits = str(n)

    def check(left, right):
        # Base case 1: If pointers cross or meet, all pairs matched! (checking indices)
        if left >= right: 
            return True
        
        # Base case 2: If characters at the pointers don't match
        if digits[left] != digits[right]: 
            return False 
            
        # Recursive step: Move pointers inward
        return check(left + 1, right - 1)

    return check(0, len(digits) - 1)

# Test cases: 
print("Test cases results: ")
values = [0, 7, 11, 123454321, 1357531, 168861]
for value in values: 
    print(isPalindromeNum(value))

values2 = [10, 112221]
for value1 in values2:
    print(isPalindromeNum(value1))


# What stops this function? 
# isPalindromeNum() stops when the left greater than or equals to the right 

# What becomes smaller?
# the right string 

# Why can returning False too early fail?