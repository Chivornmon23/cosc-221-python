# with open("message.txt", "x") as file:
#     file.write("Python is fun!")
#
# with open("message.txt", "r") as file:
#     content = file.read()
#     print(content)
#
with open("students.txt", "w") as file:
    for i in range(3):
        name = input(f"Enter student name {i + 1}: ")
        file.write(name + "\n")

print("Student names saved to students.txt")

with open("students.txt", "a") as file:
    name = input("Enter one more student name: ")
    file.write(name + "\n")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

try:
    with open("marks.txt", "qr") as file:
        file.read()
except FileNotFoundError:
    print("File does not exist")

