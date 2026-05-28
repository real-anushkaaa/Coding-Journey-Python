"""
Question:
Convert two lists into a dictionary.
"""

# Write your code here

keys = ["a", "b", "c"]
values = [1, 2, 3]

d = dict(zip(keys,values))

print(d)