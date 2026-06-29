"""
Python Constructor Practice

Question:
Create a class Student with a constructor that initializes name.
"""

# Write your solution below.

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("anushka")
print(s1.name)