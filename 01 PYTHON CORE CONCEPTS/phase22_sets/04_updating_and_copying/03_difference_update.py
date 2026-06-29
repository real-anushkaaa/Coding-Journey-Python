"""
Question:
Remove all common elements using difference_update().
"""

# Write your code here

A = {1, 2, 3, 4}
B = {3, 4, 5}

A.difference_update(B)

print(A)