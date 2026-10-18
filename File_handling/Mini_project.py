note = input("Enter your note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("\nAll saved notes: ")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
