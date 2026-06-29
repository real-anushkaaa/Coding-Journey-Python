"""
Question:
Count how many values are greater than 50.
"""

# Write your code here

numbers = {"a": 10, "b": 60, "c": 80, "d": 45}

count = 0

for value in numbers.values():
    if value > 50:
        count += 1

print(count)