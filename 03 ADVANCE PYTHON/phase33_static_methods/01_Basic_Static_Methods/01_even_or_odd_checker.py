"""
Python Static Methods Practice

Question:
Create a class NumberUtility. 
Create a static method is_even(number) that returns whether a number is even or odd.
"""

# Write your solution below.

class NumberUtility:

    @staticmethod
    def is_even(number):
        if number % 2 == 0:
            return "even"

        else:
            return "odd"

print(NumberUtility.is_even(12))