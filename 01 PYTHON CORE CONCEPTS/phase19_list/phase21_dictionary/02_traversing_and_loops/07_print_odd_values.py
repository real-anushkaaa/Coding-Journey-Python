"""
Question:
Print only odd values from a dictionary.
"""

# Write your code here

numbers = {"a": 10, "b": 15, "c": 22, "d": 31}

for value in numbers.values():
    if value % 2 != 0:
        print(value)