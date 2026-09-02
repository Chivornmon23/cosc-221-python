# Exercise 1
# Write a python program to create a tuple with different data types
my_tuple = ("Messi", 39, "Inter Miami", "Forwarder", 1.69)

# Convert the tuple to the list and print list 
convert_tuple_to_list = list(my_tuple)
print(convert_tuple_to_list)

# Add elements to the list 
convert_tuple_to_list.append("Please add me!")
convert_tuple_to_list.append("23-04-2006")

#Convert back the list to the tuple and print the tuple 
convert_list_to_tuple = tuple(convert_tuple_to_list)
print(convert_list_to_tuple)

#Check whether the birth date exists
print("23-04-2006" in convert_list_to_tuple)

# Find the length of the tuple 
print(f"The length of the tuple is: {len(convert_list_to_tuple)}")

