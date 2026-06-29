"""
Python OOP Practice

Question:
Create a class Animal with a method sound(). Override it in the Dog class.
"""

# Write your solution below.

class Animal:
    def sound(self):
        print("animals have different sounds")

class Dog(Animal):
    def sound(self):
        print("dog says : wooffff")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()