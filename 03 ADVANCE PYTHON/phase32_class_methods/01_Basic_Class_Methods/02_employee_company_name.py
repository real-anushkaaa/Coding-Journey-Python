"""
Python Class Methods Practice

Question:
Create a class Employee. 
Store the company name as a class variable. 
Create a class method change_company(new_name) to update the company name for all employees.
"""

# Write your solution below.

class Employee:
    company = "HP"
    
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name
        print(f"new company : {cls.company}")
        
Employee.change_company("GOOGLE")

