# Exercise 4: Real-World Application
# 1. Create a gradebook with the following:
grade_book = {
    "John": 85,
    "Mary": 92,
    "Paul": 78,
    "Anna": 89,
    "Steve": 95
}
# 2. Create function to calculate the average grade
def calculate_avg(grades): 
    return sum(grade_book.values())/len(grade_book)

# 3. Create function to find the student with the highest grade
def find_highest_grade(grades): 
    return max(grades, key=grades.get)
