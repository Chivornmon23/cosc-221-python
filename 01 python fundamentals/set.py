# set = collection with is unordered, unindexed. No duplicate values

utensils = {"fork", "Spoon", "Knife"}
dishes = {"Bowl", "Plate", "Cup"}
#Add the element to the set
utensils.add("Bowl")

# Remove the element
utensils.remove("fork")

#Clear all the element
# utensils.clear()

#Add all the element from one set to another 
# dishes.update(utensils)

#Join new set together and create a new one entirely
dinner_table = utensils.union(dishes) 
# or
# dinner_table = dishes.union(utensils)


# compare the two sets 
print(dishes.difference(utensils)) #in this case, we want to compare what dishes has and utensils doesnt have 

print(dishes.intersection(utensils))  # find the element in common
# for x in dishes: 
#     print(x)
