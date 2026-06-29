"""
Python Constructor Practice

Question:
Create a class Car with default model 'Not Assigned'.
"""

# Write your solution below.

class Car:
    def __init__(self, model = "Not Assigned"):
        self.model = model

c1 = Car()
c2 = Car("BMW X5")
print(c1.model)
print(c2.model)