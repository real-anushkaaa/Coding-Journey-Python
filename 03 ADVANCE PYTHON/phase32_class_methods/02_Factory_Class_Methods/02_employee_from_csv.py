"""
Python Class Methods Practice

Question:
Create a class Employee. 
Create a class method that creates an object from a comma-separated string such as 
'101,Rahul,45000'.
"""

# Write your solution below.

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        id, name, salary = data.split(",")
        return cls(int(id), name, int(salary))
    
e1 = Employee.from_string("101,rahul,45000")
print(e1.id,e1.name,e1.salary)