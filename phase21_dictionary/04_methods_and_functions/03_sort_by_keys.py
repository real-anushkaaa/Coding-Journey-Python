"""
Question:
Sort dictionary by keys.
"""

# Write your code here

data = {"b": 2, "a": 1, "c": 3}

new_dict = dict(sorted(data.items()))

print(new_dict)