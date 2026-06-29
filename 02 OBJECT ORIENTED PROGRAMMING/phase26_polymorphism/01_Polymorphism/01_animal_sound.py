"""
Python OOP Practice

Question:
Create a base class Animal with a method sound(). Create child classes Dog, Cat, and Cow, 
each providing its own implementation of sound(). Call the method using a loop.
"""

# Write your solution below.

class Animal:
    def sound(self):
        print("animal makes different sounds")

class Dog(Animal):
    def sound(self):
        print("woof")

class Cat(Animal):
    def sound(self):
        print("meoww")

class Cow(Animal):
    def sound(self):
        print("cowwwwww")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()