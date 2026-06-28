"""
Python Inheritance Practice

Question:
Create a Person class and initialize Student using super().
"""

# Write your solution below.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_num):
        super().__init__(name)
        self.roll_num = roll_num

c1 = Student("anushka","23100BTCSE14787")
print(c1.name)
print(c1.roll_num)