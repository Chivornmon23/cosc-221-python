# Exercise 1: 
# 1. Create a dictionary with 5 students

students = {202501: "Chivorn", 202502: "Dara", 202503: "Vuthy", 202504: "Kimseang", 202505: "Panha"}
print(f"5 students in the dictionary: {students}")

# 2. Add two new students 
students[202506] = "Sreynith"
students[202507] = "Limey"
print(f" Add two new studnets: {students}")

# 3. Modify the name of an existing student
students[202501] = "Messi"
print(f"Modify the name of Chivorn to Messi {students}")

# Delete a student using their id
del students[202501]
print(f"Student id 202501 has been deleted: {students}")

# Retrieving a non-existing student and demostrate KeyError
print(students[999])

