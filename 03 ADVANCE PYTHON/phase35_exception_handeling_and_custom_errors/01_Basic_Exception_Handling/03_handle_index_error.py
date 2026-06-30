"""
Python Exception Handling and Custom Errors Practice

Question:
Handle an IndexError when accessing a list element.
"""

# Write your solution below.

try:
    a = [10,20,30]
    print(a[6])

except IndexError:
    print("write correct index value")