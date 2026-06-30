"""
Python Class Methods Practice

Question:
Create a class Student. 
Maintain the total number of students using a class variable. 
Create a class method total_students() that displays the total count.
"""

# Write your solution below.

class Student:
    total = 0
    
    def __init__(self, name):
        self.name = name
        Student.total += 1

    @classmethod
    def total_students(cls):
        print(f"total student : {cls.total} ")

e1 = Student("anushka")
e2 = Student("anu")
e3 = Student("anus")
e4 = Student("anusha")
e5 = Student("anuska")

Student.total_students()