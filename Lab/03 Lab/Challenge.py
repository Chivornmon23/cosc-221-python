# 1. Problem Description:
# You are tasked with creating a system to manage student information for a
# course. The system will handle:
# 1. Adding students and their grades.
# 2. Calculating the average grade of the class.
# 3. Displaying the student with the highest grade.
# 4. Displaying the list of students who passed or failed based on their
# grades.
# 2. Requirements:
# 1. Create a dictionary called courses, where each key represents a course
# name (e.g., "Math", "Physics", "Chemistry") and the value is another
# dictionary that stores student names as keys and their grades as values.

# 2. Each course should have 3 students, and the grades should be random
# values between 0 and 100.

# 3. Implement a function of average_grade that calculates and returns the
# average grade of all students in a course.
import random
courses = {
    "Math"  : {
        "Chivorn"  : random.randint(0,100),
        "Messi"     : random.randint(0,100),
        "Bopha"     : random.randint(0,100)
    },
    "Physics" : {
        "Chivorn"  : random.randint(0,100),
        "Messi"     : random.randint(0,100),
        "Bopha"     : random.randint(0,100)
    },
    "Chemistry": {
        "Chivorn"  : random.randint(0,100),
        "Messi"     : random.randint(0,100),
        "Bopha"     : random.randint(0,100)
    }
}

def average_grade(course_name): 
    grades = courses[course_name].values()
    return sum(grades)/len(grades)

def highest_grade(course_name):
    course_grades = courses[course_name]
    return max(course_grades, key=course_grades.get) 

def passing_students(course_name): 
    passing = set()
    for name, grade in courses[course_name].items(): 
        if grade >= 50:
            passing.add(name)
    return passing  

def failed_students(course_name): 
    failed = set()
    for name, grade in courses[course_name].items():
        if grade < 50: 
            failed.add(name)
    return failed

print(f"The average score of Chemistry: {average_grade("Chemistry")}")
print(f"The higest score in Chemistry: {highest_grade("Chemistry")}")
print(f"The passed student in Chemisty: {passing_students("Chemistry")}")
print(f"The failed student in Chemistry: {failed_students("Chemistry")}")