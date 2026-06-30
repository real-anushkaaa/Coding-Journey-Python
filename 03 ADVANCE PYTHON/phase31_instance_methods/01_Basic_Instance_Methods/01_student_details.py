"""
Python Instance Methods Practice

Question:
Create a class Student with attributes name and age. 
Create an instance method display_details() that prints both values.
"""

# Write your solution below.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"name of the student is {self.name} and age is {self.age}")

s1 = Student("anushka",20)
s1.display_details()