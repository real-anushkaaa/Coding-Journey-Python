"""
Python Instance Methods Practice

Question:
Create a class Employee with attributes name and monthly_salary. 
Create an instance method calculate_annual_salary().
"""

# Write your solution below.

class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def claculate_annual_salary(self):
        annual_salary = self.monthly_salary * 12
        print(f"name is {self.name}, and salary is {annual_salary}")

e1 = Employee("anushka",50000)
e1.claculate_annual_salary()