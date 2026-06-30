"""
Python Exception Handling and Custom Errors Practice

Question:
Use finally to display a completion message.
"""

# Write your solution below.

try:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    c = a / b
    print(c)

except Exception as e:
    print("Invalid error:", e)

finally:
    print("This is correct")