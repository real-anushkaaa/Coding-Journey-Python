"""
Question:
Count even numbers in a set.
"""

# Write your code here

# 13. Count even numbers in a set.
numbers = {10, 15, 20, 25, 30}

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)
