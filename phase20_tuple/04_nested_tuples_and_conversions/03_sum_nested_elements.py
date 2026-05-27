"""
Question:
Find sum of all elements in nested tuples.
"""

# Write your code here

t = ((1,2),(3,4))
total = 0

for i in t:
    total = total + sum(i)

print(total)