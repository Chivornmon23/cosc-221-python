# Set is a built-in data types in Python used to store collections of data
# Sets do not allow duplicates and do not maintain any specific order

# Create set
# You can create a set of elements by enclosing the elements inside a pair of curly braces ({})

my_set = {"apple", "banana", "Cherry"}
print(my_set)

s1 = set() # Create set with empty element
s2 = set([1,2,4]) # Create a set from a tuple
s3 = set({x*2 for x in range (1, 10)}) # Create a set from a list

# You cannot access items in a set by referring to an index or a key. 
# but you can loop through the set items using a for loop or ask if a specified value 
# is present in a set, by using the in keyword. 

# loop through each items
for a in my_set: 
    print(a)

# Access set (return with true and false)
print("apple" in  my_set)
print("orange" in my_set)

# Add item to set 
my_set.add("Orange")
print(my_set)

#Concatenation Set

#There are several ways to join two or more sets in Python. 
# The union () and update() methods joiins all items from both sets


# The intersection () method keeps only the duplicates. 


# The difference() method keeps the items from the first set that are in the other set(s)


# The symmetric_difference() method keeps all items EXCEPT the duplicates. 

