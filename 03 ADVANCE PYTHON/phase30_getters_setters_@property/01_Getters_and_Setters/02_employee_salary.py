"""
Python Getters, Setters and @property Practice

Question:
Create a class Employee with a private attribute __salary. 
Implement getter and setter methods. 
Reject negative salaries.
"""

# Write your solution below.

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary 
    
    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("reject negative salaries")

e1 = Employee(500000)
print(e1.get_salary())

e1.set_salary(1000000)
print(e1.get_salary())

e1.set_salary(-1000000)
print(e1.get_salary())