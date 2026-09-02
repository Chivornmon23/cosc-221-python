# Challenging Exercise 1

#Create a tuple with some student names
my_students = ("Messi", "Ronaldo", "Neymar", "Lamine", "Mbappe", "Bellingham", "Messi")
print(f"This is a list of student names: {my_students}. And 'Messi' duplicates")

# Covert a tuple to a set
my_set_students = set(my_students)
# Messi is automantically removed 
print(f"Set after removing 'Messi': {my_set_students}")

# Search for a name in the set 
name = input("Enter a name to search: ")

if name in my_set_students: 
    print(f"{name} exists in the set")
else: 
    print(f"Student named {name} doesnt exist.")

choice = input("Do you want to add / remove? (a/r): ")

if choice == "a": 
    name = input("Enter a name to add: ")
    my_set_students.add(name)
elif choice == "r": 
    name = input("Enter a name to remove: ")
    my_set_students.remove(name)
else: 
    print("Invalid input")

print(my_set_students)

with open("students.txt", "w") as file: 
    file.write(str(my_set_students))
print("Names saved to file.")

with open("students.txt", "r") as file:
    loaded_names = file.read()
print(f"Names loaded from file: {loaded_names}")