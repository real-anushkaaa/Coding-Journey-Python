"""
Python Exception Handling and Custom Errors Practice

Question:
Use else after successful division.
"""

# Write your solution below.

try:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    c = a / b
    print(c)

except Exception as e:
    print("Invalid error:", e)

else:
    print("This is correct")