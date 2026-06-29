"""
Python Inheritance Practice

Question:
Create a class Vehicle and inherit it into a class Car.
"""

# Write your solution below.

class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    pass

c1 = Car()
c1.start()