"""
Python Constructor Practice

Question:
Create a class Student with a constructor that initializes name and age.
"""

# Write your solution below.

class Student:
    def __init__(self, name , age):
        self.name = name
        self.age = age

s1 = Student("anushka",20)
print(s1.name)
print(s1.age)