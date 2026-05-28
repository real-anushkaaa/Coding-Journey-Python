"""
Question:
Replace negative values with 0.
"""

# Write your code here

numbers = {"a": -5, "b": 10, "c": -8}

for key in numbers:
    if numbers[key] < 0:
        numbers[key] = 0

print(numbers)