"""
Question:
Merge two tuples without using +.
"""

# Write your code here

t1 = (1, 2)
t2 = (3, 4)

result = tuple(list(t1)+list(t2))

print(result)