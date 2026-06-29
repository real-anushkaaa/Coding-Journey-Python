"""
Python OOP Practice

Question:
Create a class Calculator with an add() method that can add two or three numbers.
"""

# Write your solution below.

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, c):
        return Calculator((self.x + c.x),(self.y + c.y))
    
    def display(self):
        print(self.x, self.y)

c1 = Calculator(20,10)
c2 = Calculator(5,10)
  
c3 = c1 + c2
c3.display()