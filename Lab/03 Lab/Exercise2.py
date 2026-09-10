# Exercise 2: Dictionary methods

# 1. Use the keys() method to display all student IDs.
students = {202501: "Chivorn", 202502: "Dara", 202503: "Vuthy", 202504: "Kimseang", 202505: "Panha"}
print(f"These are all the students' IDs: {tuple(students.keys())}")

# 2. Use the values() method to display all student names.
print(f"These are all the students' names: {tuple(students.values())}")

#3. Use the items() method to display student ID and name pairs.
print(f"These are students info: {tuple(students.items())}")

# 4. Use the get() method to retrieve a student’s name and handle 
# a non-existing student.
result = students.get("Limey", "Not Found")

if result == "Not Found":
    print("That student name does not exist in the system.")
else:
    print(f"Student found: {result}")

# 5. Use the pop() method to remove a student by their ID.
print(f"Remove student ID: 202501: {students.pop(202501)} from the system")
print(f"The updated dict: {students}")

#6. Use the clear() method to remove all entries from the dictionary.
print(f"Clear all students: {students.clear()}")
