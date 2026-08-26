# Student Grade Record Manager

info = ("Software Development", 3.5 , "Java", "Python", "Networking", "Java")

#Create a subtuble to store the sliced element from the info tuple 
courses = info[2:6]
print(f"The courses are: {courses}")

for i, x in (enumerate(info)):
    # enumerate () is a built-in python function that takes an iterable (like a list, tuple
    #   or string) and returns an enumerate object yielding pairs containing a counter 
    #   (index, starting at 0 by default) and the corresponding value from the iterable 
    print(f"({i}). {x}")

indices = [i for i, course in enumerate(courses) if course == "Java"]
print(indices)
    



