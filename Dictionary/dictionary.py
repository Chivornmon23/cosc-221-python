# dictionary used to store key/value pairs
# provides quick access to elements using keys. 
# a dictionary cannot contain duplicate keys

my_dict = {"name": "Alice", "age" : 20}

# To create empty dictionary 
empty_dict = {}

# To create empty set 
empty_set = set()

# Key must be hasable meaning only numbers, string, etcs. 
# Value can be any type 

# Creating dictionary 
my_dict1 = {1: "one", 2: "two"} #Numbers are okay
my_dict2 = {"name": "Alice", "age": 20} #String are okay
my_dict3 = {(1,2): "point", (6, 7): "point1"} #Tuples are okay

# Adding element
my_dict1[3] = "three"
# print(my_dict1)

# Modifying items
# If the key alr exists, assigning a new value to the key will replace the old value
my_dict[3] = "five"
#print(my_dict1)

#Retrieving  
print(my_dict[3])

# Deleting item 
del my_dict1[2]
print(my_dict1)

if 1 in my_dict1:
    del my_dict1[1]
else: 
    print("Key Not Found!")

print(my_dict1)

#Dictionary Method
print(my_dict2)
# 1 Keys()
# Returns: A sequence of the dictionary's keys as a tuple.
print(f"Using keys() method: {tuple(my_dict2.keys())}")

# 2 values()
# Returns: A sequence of the dictionary's values as a tuple.
print(f"Using values() method: {tuple(my_dict2.values())}")

# 3 items()
# Returns: A sequence of tuples, where each tuple is in the form (key, value).
print(f"Using items() method: {tuple(my_dict2.items())}")

# 4 get(key)
# Returns: The value for the specified key.
# If the key does not exist, it returns None instead of raising a KeyError.
print(my_dict2.get("name")) #Output: Alice
print(my_dict2.get("age")) # Output: 20

# 4 pop (key)
# Returns: The value for the specified key, and removes the item from the dictionary
print(f"before pop(): {my_dict2}")

print(my_dict2.pop("name")) #output Alice

print(f"after pop(): {my_dict2}")

# 6 popitem()
# Returns: A randomly selected (key, value) pair as a tuple, and removes the selected item from the dictionary.
print(my_dict3)

print(my_dict3.popitem())

print(f"After popitem(): {my_dict3}")

# 7 clear()
# Returns: removes all items from the dictionary.
my_dict3.clear()
print(f"After clear(): {my_dict3}")

# Application of dictionary

# 1. Employee dictionary: 
employee = {
    "E123" : {"name": "Chivorn", "position": "Engineer"},
    "E124" : {"name": "Messi", "position": "Manager"}
}
print(employee)

# 2. Web Scraping and Data Organization 
product_data = { 
    "101": {"name": "Laptop", "price": 1200, "avaiability": "In stock"},
    "102": {"name": "iPhone", "price": 1300, "avaiability": "Out of stock"},
    "103": {"name": "MacBook", "price": 1400, "avaiability": "In stock"}
}
print(product_data)