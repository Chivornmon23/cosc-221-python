#Exercise 2

# Create a tuple containing at least 5 numbers and print the first and the last
my_tuple = (1, 3, 4, 5, 6)

print(f"The first element is: {my_tuple[0]}")
print(f"The last element is : {my_tuple[-1]}")

# Create two sets of numbers 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#Perform union, intersection, difference method 
set_union = set1.union(set2)
set_intersection = set1.intersection(set2)
set_difference = set1.difference(set2)
set_difference2 = set2.difference(set1)

#Display result of each operation 
print(f"The union element of both sets are: {set_union}")
print(f"The intersection element of both sets are: {set_intersection}")
print(f"The difference element between set1 and set2 are {set_difference}")
print(f"The difference element between set 2 with set 1 is {set_difference2}")

