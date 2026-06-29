"""
Question:
Find frequency of all elements in a tuple.
"""

# Write your code here

t = (1,2,2,3,1,4)

for i in set(t):
    print(i, "=", t.count(i))