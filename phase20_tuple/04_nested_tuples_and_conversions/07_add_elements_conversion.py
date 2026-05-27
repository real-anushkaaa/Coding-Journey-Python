"""
Question:
Add elements after converting tuple into list.
"""

# Write your code here

t = (1,2,3,4,5)

l = list(t)

l.append(7)

t = tuple(l)

print(t)