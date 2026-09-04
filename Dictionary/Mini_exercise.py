# Mini Exercise 
# 1. Create a dictionary with the following student grades: 

my_students = {"John": 85, "Sarah": 92, "Alex": 78, "Linda": 88, "David": 95}
print(f"Dictionary of my students: {my_students}")
# Add a new student
my_students["Emily"] = 91
print(f"Updated dictionary of my student after added a new student: {my_students}")
# Modify Sarah's grade to 95
my_students["Sarah"] = 95
print(f"Updated dictionary of my student after modified Sarah's grade: {my_students}")
# Remove Alex from the dictionary
if "Alex" in my_students:
    del my_students["Alex"]
    print(f"Updated dictionary of my student after deleted Alex's key: {my_students}")
else: 
    print("Key not found.")

# Print student who score above 90
print("Names of students who scored above 90: ")
for student in my_students: 
    if my_students.get(student) > 90: 
        print(student)