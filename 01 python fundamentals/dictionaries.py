# Dictionaries = a collection of {key:value} pairs ordered and changeable. No duplicate.

capitals = {"USA" : "Washington D.C", 
            "India" : "New Delhi", 
            "China" : "Bejing", 
            "Russia" : "Moscow"
}

# print(dir(capitals))
# print(help(capitals))

# to get the value
print(capitals.get("USA"))

# To check the key exists or not?
if capitals.get("Russia"): 
    print("That capital exists")
else: 
    print("That capital doesn't exist")

# to update the dictionaries 
capitals.update({"Germany": "Berlin"})
capitals.update({"Germany": "Detroit"})

#to move the key from the dictionaries
capitals.pop("China")

#to move the latest key 
capitals.popitem()

print(capitals)

# #clear the dictionaries
capitals.clear()
print(capitals)

# to get all the keys in the dictionary but not the value
keys = capitals.keys()

for key in capitals.keys(): 
    print(key)

# to get all the values in the dictionary but not the keys
values = capitals.values()

for value in capitals.values(): 
    print(value)

# return a dictionary obj which resembles a list of tuples [(), (), ()]
items = capitals.items()
for key, value in capitals.items(): 
    print(f"{key}: {value}")