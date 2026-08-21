# function = A block of reuseable code place () after the function name to invoke it

def happy_birthday(name, age): 
    print(f"Happy birthday to you, {name}!")
    print(f"You are {age} old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Messi", 39)
happy_birthday("Ronaldo", 41)

def display_invoice(username, amount, due_date): 
    print(f"Hello, {username}!")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

#invoke a function 
display_invoice("Messi", 100.74, "23-04-2026" )

#return = statement used to end a function and send a result back to the caller 

def add(x, y): 
    z = x+y
    return z

print(add(2,2))


def create_name(first, last): 
    first = first.capitalize()
    last = last.capitalize()

    return first + " " + last

full_name = create_name("Leo", "Messi")
print(full_name)

#Default arguments = A default value for certain parameters 
# default is used when that argument is omitted 
# make your functions more flexiable, reduces # of arguments 
#   1. positional, 2. Default, 3. Keyword, 4. arbitrary

def net_price (list_price, discount = 0, tax = 0.05): 
    return list_price * (1 - discount) * (1 + tax)

print(f"This is a net price: {net_price(500)}")
print(f"This is a net price with 10% discount: {net_price(500, 0.1)}")
print(f"This is a net price with 10% discount and tax: {net_price(500, 0.1, 0.5)}")

import time

def count(start, end): 
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("FUCK YOU!")

count(0,1)