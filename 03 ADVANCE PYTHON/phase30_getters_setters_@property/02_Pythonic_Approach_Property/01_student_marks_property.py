"""
Python Getters, Setters and @property Practice

Question:
Create a class Student with a private attribute __marks. 
Use @property and @marks.setter. 
Validate that marks are between 0 and 100.
"""

# Write your solution below.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("invalid marks")

s1 = Student(70)
print(s1.marks)

s1.marks = 30
print(s1.marks)

