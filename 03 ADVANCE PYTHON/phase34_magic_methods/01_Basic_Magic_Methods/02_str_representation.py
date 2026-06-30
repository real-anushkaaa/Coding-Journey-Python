"""
Python Magic Methods Practice

Question:
Create a class Book. 
Override the __str__() method. 
Print the object directly using print(book).
"""

# Write your solution below.

class Book:
    def __init__(self, author, prize):
        self.author = author
        self.prize = prize

    def __str__(self):
        return f"Book : {self.author}, {self.prize}"

b1 = Book("anushka",450)
print(str(b1))