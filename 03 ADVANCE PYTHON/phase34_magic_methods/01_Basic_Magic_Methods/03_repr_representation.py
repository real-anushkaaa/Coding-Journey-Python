"""
Python Magic Methods Practice

Question:
Create a class Employee. Override the __repr__() method. Display the object in a developer-friendly format.
"""

# Write your solution below.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

e1 = Employee("Anushka", 50000)

print(repr(e1))
print(e1)