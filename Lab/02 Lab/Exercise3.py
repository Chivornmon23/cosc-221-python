# Exercise 

# Write a program that ask the user to input three values 

my_tuple = ()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

my_tuple = (name, age, city)
print(my_tuple)

# Count tuple 
print(f"Count of 'messi in the tuple: {my_tuple.count("messi")}")

# Find index
print(f"Index of 'Phnom Penh' in the tuple: {my_tuple.index("Phnom Penh")}")


