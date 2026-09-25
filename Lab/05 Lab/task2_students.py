def push_qualified(students, stack):
    #TODO: loop through students.items()
    for name, mark in students.items(): 
        if mark >= 75: 
            stack.append(name)

def pop_all(stack):
    #TODO: collect and return poppeed names
    popped_names = []
    while len(stack) > 0:
        popped_names.append(stack.pop())
    return popped_names

students = {"Vanna": 100, "Tena": 100, "Devi": 100, "Mina": 100, "Sok": 100,}

stack = []
#TODO: call the functions and print the results

#1. push_qualified: append qualifying names in dictionary insertion order. Pass in an initially empty stack and call once. 
push_qualified(students, stack)
print("Stack before popping: ", stack)

returned_name = pop_all(stack)
print(f"Returned name: {returned_name}")
print(f"The original stack is now empty: {stack}")

#Check and explain 

# Test mark of 74 will be skipped because the condition mark >= 75
# Test mark of 75 will be added to the stack (inclusive boundary)
# Test mark of 76 will be added to the stack 
#  an empty dictionary: the loop wont execute and leaving the stack and returned_name empty
# nobody qualify: the two stacks remain empty 
# everybody qualified: the stack stores everyone and the returned_name stores every name but reverse order from stack.

# 75 is an important test because it represents boundary value. Testing it ensures the 
# conditional logic correctly uses >= rather than strictly > 

#What happens when a dictionary key is reused?
# In Python dictionaries, keys must be unique. 
# If you assign a value to an existing key, the new value will
# overwrite the old value rather than creating a duplicate entry.


