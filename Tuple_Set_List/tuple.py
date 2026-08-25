# Tuple is a built-in data types in Python used to store collections of data
# Tuples are similar to lists
# This collection also has iterable, ordered, and (can contain) repetitive data, just like lists
# But unlike lists, tuples are immutable (unchangeable)

# Create tuple
t1 = ()  #create an empty 
t2 = (1, 2, 3) #create a tuple with three elements
t3 = (1,2, 'abc', 3, 4) #create a tuple with mulitple data type
t4 = tuple((1, 3, 5, "Hello")) #create a tuple with the tuple() constructor
t6 = tuple([2 * x for x in range (1,5)]) #create a tuple from a list 

# using tuple() keyword to convert list to tuple 

my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)

# Access tuple 
#Indexing 
tuple1 = (1, 2, "Hello", 3)
print(f" at index 2: {tuple1[2]}")

print(f"The last item: {tuple1[-1]}")

#Update Tuple 
my_tuple = ("Mat Nab", 27, 1.5, "Cambodia")
#Convert the tuple to list 
convert_tuple_to_list = list(my_tuple)
print(f" before converting: {convert_tuple_to_list}")
#Change the item
convert_tuple_to_list[1] = 30
print(f" after converting: {convert_tuple_to_list}")

#Concatenation Tuple 
# Joun Tuple 
tuple = t1 + t2 + t3
print(f"Concatenation: {tuple}")

#Tuple method 
# Python has two built-in methodss that you can use on tuples index() and count()

#1 index
my_tuple1 = (1, 2, 4, 5, 6, 7, 8, 9, 3, 2)
y = my_tuple1.index(8)
print(y)

# count()
y = my_tuple1.count(2)
print(y)