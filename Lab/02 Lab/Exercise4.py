# Exercise 4

#Take a list of numbers, convert it to a set and display the set 

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

my_set = set(my_list)
print(my_set)

# Write a program to add 10, 20, 30 to a set 
my_set.update([10, 20, 30])
print(my_set)

# Convert a set to list 
my_converted_set_to_list = list(my_set)
# Remove the last three items at once 
print(my_converted_set_to_list[:-3])
