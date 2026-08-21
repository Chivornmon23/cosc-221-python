# Tuples = collection which is ordered and unchangeable used to group together related data

student = ("Bro", 21, "male")

#Access tuple

# count how many value appear in the tuple 
print(student.count("Bro"))

# find at what index the value locates in the tuple 
print(student.index("male"))

# using for loop to print all the values in the tuple 

for x in student: 
    print(x)

if "Bro" in student: 
    print("Bro is here ")