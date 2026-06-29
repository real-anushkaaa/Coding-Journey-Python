"""
Question:
Sort dictionary by values.
"""

# Write your code here

data = {"a": 30, "b": 10, "c": 20}

new_dict = dict(sorted(data.items(),
        key = lambda item: item[1]))

print(new_dict)