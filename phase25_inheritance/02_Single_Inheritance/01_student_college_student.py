"""
Python Inheritance Practice

Question:
Create a class Student with constructor and inherit it into CollegeStudent.
"""

# Write your solution below.

class Student:
    def __init__(self):
        print("Student constructor called.")

class CollegeStudent(Student):
    pass

c1 = CollegeStudent()