"""
Question:
Find common keys between two dictionaries.
"""

# Write your code here

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

common_keys = d1.keys() & d2.keys() # '&' means intersection (common elements)

print(common_keys)