"""
Question:
Find sum of values in nested dictionary.
"""

# Write your code here

data = {
    "a": {"x": 10, "y": 20},
    "b": {"x": 30, "y": 40}
}

total = 0

for inner_dict in data.values():
    total += sum(inner_dict.values())

print(total)