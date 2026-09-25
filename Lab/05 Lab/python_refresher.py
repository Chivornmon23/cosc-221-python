class Student: 
    def __init__(self, name): 
        self.name = name 
    def greet(self): 
        return "Hello, " + self.name 

first = Student("Vanna") 
second = Student("Tena")   
first.name = "Mina"

print(first.name)
print(second.greet())