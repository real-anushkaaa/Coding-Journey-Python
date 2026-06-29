"""
Python Inheritance Practice

Question:
Create a parent class constructor and initialize it using super().
"""

# Write your solution below.

class Parent:
    def __init__(self):
        print("parent constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("child constructor cslled")

c1 = Child()