"""
Python Exception Handling and Custom Errors Practice

Question:
Write a program that safely divides two numbers using try-except.
"""

# Write your solution below.

try:
    a = int(input("enter ethe 1st number"))
    b = int(input("enter ethe 2st number"))
    c = a/b
    print(c)

except ValueError:
    print("Invalid input! Please enter integers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")