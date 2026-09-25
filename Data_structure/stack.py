# We use stack to reverse data (undo operation)

#important operation 
# 1. push() : add an object to the top of the stack 
# 2. pop(): remove and return the top object from the stack 
# 3. top(): Access (but do not remove ) the top object

#Problem 1: Reversing a String Using a Stack
def reverse_string(s):
    stack = []
    
    # Push phase: push each character onto the stack
    for char in s:
        stack.append(char)
        
    # Pop phase: pop each character to build the reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
        
    return reversed_str

print(reverse_string("chivornmon"))

# Problem 2: Balancing Parentheses Using a Stack
def is_balanced(expression):
    stack = []
    # Dictionary to hold matching pairs
    matching_pairs = {')': '(', '}': '{', ']': '[', '<':'>', "'": "'", '"': "'"}

    for char in expression:
        if char in matching_pairs.values():  # If it's one of the opening symbols
            stack.append(char)
        elif char in matching_pairs.keys():  # If it's one of the closing symbols
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False

    return len(stack) == 0

# Test cases
expression1 = "{[()()]}"
expression2 = "{[(])}"

print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

x