"""
Python Exception Handling and Custom Errors Practice

Question:
Raise a ValueError if age is less than 18.
"""

# Write your solution below.

def check_age(age):
    if age < 18:
        raise ValueError("age must be 18 or older")
    return "Access granted"

try:
    print(check_age(20))
    print(check_age(30))
    print(check_age(10))
    print(check_age(40))

except ValueError as e:
    print(f"error : {e}")
