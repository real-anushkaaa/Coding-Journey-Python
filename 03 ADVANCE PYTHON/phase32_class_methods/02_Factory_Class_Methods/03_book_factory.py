"""
Python Class Methods Practice

Question:
Create a class Book. 
Create a class method that creates a Book object from a dictionary.
"""

# Write your solution below.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['author'], data['price'])
    
book_data = {
        "title" : "the sky is pink",
        "author" : "anushka",
        "price" : 20
        }
    
b1 = Book.from_dict(book_data)

print(b1.title)
print(b1.author)
print(b1.price)