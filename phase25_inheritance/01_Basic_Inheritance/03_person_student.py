"""
Python Inheritance Practice

Question:
Create a class Person with a method display(). Inherit it into Student.
"""

# Write your solution below.

class Person:
    def display(self):
        print("i am a person")

class Student(Person):
    pass

s1 = Student()

s1.display()