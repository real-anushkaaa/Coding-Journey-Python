"""
Python Getters, Setters and @property Practice

Question:
Create a class Student with a private attribute __marks. 
Implement set_marks() and get_marks(). 
Do not allow marks below 0 or above 100.
"""

# Write your solution below.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
    def set_marks(self, new_marks):
        self.__marks = new_marks

s1 = Student(87)
print(s1.get_marks())

s1.set_marks(97)
print(s1.get_marks())

