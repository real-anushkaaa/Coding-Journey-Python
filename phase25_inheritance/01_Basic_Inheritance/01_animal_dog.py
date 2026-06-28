"""
Python Inheritance Practice

Question:
Create a class Animal with a method eat(). Create a class Dog that inherits from Animal.
"""

# Write your solution below.

class Animal:
    def eat(self):
        print("animal is eating")
    
class Dog(Animal):
    pass

d1 = Dog()

d1.eat()