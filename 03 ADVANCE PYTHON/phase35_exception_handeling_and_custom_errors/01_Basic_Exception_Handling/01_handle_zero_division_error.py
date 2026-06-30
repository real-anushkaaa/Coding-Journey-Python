"""
Python Exception Handling and Custom Errors Practice

Question:
Write a program to handle a ZeroDivisionError.
"""

# Write your solution below.

try:
    x = 10/0
except ZeroDivisionError:
    print("not div by 0")