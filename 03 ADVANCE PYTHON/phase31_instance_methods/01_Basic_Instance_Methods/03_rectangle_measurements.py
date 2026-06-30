"""
Python Instance Methods Practice

Question:
Create a class Rectangle with attributes length and width. 
Create instance methods area() and perimeter().
"""

# Write your solution below.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"area of rect is : {area}")

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"perimeter of rect is : {perimeter}")

r1 = Rectangle(10,20)
r1.area()
r1.perimeter()