"""
Python Constructor Practice

Question:
Create a class Car with a constructor that initializes brand and model.
"""

# Write your solution below.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("BMW","X5")
print(c1.brand)
print(c1.model)