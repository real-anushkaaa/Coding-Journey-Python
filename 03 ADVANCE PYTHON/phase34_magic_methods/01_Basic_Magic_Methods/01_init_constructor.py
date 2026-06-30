"""
Python Magic Methods Practice

Question:
Create a class Student. 
Implement the __init__() magic method to initialize name and age. 
Create an object and display the values.
"""

# Write your solution below.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("anushka",20)
print(s1.name)
print(s1.age)