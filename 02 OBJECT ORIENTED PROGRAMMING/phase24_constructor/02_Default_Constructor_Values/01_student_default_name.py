"""
Python Constructor Practice

Question:
Create a class Student with default name 'Unknown'.
"""

# Write your solution below.

class Student:
    def __init__(self, name = "Unknown"):
        self.name = name

s1 = Student()
s2 = Student("anushka")

print(s1.name)
print(s2.name)