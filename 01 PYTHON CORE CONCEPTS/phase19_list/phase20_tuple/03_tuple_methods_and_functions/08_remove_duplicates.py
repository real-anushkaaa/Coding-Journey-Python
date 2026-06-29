"""
Question:
Remove duplicate elements from a tuple.
"""

# Write your code here

t = (1, 2, 2, 3, 4, 4)

result = tuple(set(t))

print(result)