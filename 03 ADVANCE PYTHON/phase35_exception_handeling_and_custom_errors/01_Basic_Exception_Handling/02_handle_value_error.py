"""
Python Exception Handling and Custom Errors Practice

Question:
Write a program to handle a ValueError while converting user input to an integer.
"""

# Write your solution below.

try:
   x = int(input("enter the 1st number :"))
   y = int(input("enter the 2nd number :"))
   z=x+y
   print(z)

except ValueError:
   print("invalid input")