"""
Python Class Methods Practice

Question:
Create a class Student. 
Create a class method from_string() that creates an object from a string like 'Anushka-20-BCA'.
"""

# Write your solution below.

class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    @classmethod
    def from_string(cls, data):
        name, age, department = data.split("-")
        return cls(name, int(age), department)
    
s1 = Student.from_string("anushka-20-B.tech")

print(s1.name, s1.age, s1.department)