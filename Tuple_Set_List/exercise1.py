fav_foods = ["pizza", "hamburger", "sandwich", "spagetti", "curry"]

print("The first food: ", fav_foods[1])
print("The last food: ", fav_foods[-1])
print()

numbers = [1,2, 3, 2, 4, 1, 5]
numbers_list = set(numbers)
print(f"Duplicates removed: ", numbers_list)
print()

students = {"Name": "Chivorn",
            "Age": 20,
            "Score": 100}
print(students)

students['Score'] = 99

print()
print(f"Modified Score from 100 to {students["Score"]}")
print(students)

print()
print("====Mini Challenge====")
my_stud = {"Chivorn": 100,
           "LeangY": 99,
           "Limey": 98
           }
print("Displaying students and their scores: ")
for key, value in my_stud.items():
    print(key, value)
