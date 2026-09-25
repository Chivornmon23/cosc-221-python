

def push (stack, value):
    #TODO: add value to the top 
    stack.append(value)
    
def pop(stack):
    #TODO: return the top number, or None if empty 
    if is_empty(stack):
        return None
    return stack.pop()

def is_empty(stack):
    #TODO: return True or False
    return len(stack) == 0

stack = []
#TODO: perform the operations and print the results
# 1. Push 5, 10, 15
push(stack, 5)
print("After pushing 5: ", stack)

push(stack, 10)
print("After pushing 10: ", stack)

push(stack, 15)
print("After pushing 15: ", stack)

#2. Pop one number and record the returned value. 
popped_value = pop(stack)
print(f"Popped value: {popped_value}, stack after pop: {stack}")

#3 Check whether the stqck is empty 
empty_check = is_empty(stack)
print("The stack is empty: ", {empty_check})

# 4 push 20 and print the stack 
push(stack, 20)
print(f"Final stack - After pushing 20: ", stack)

# Check and explain 

# Test an empty stack and a stack with one number 
empty_stack = []

popped_value_from_empty_stack = pop(empty_stack)
print(f"Popped value from the empty stack: {popped_value_from_empty_stack}")
stack1 = [1]
popped_value_from_one_value_stack = pop(stack1)
print(f"Popped value from the stack with 1 value: {popped_value_from_one_value_stack}")

# Why does 15 leave first?
# because stack follows the LIFO principle 
# Since 15 was the last element pushed onto the stack. 

# How does return differ from print?
# return sends a value back to the caller function so it can be stored in a variable, 
# reused, or further evaluated 

# print() outputs text or data to the terminal and it does not pass data 
# back to the program 



