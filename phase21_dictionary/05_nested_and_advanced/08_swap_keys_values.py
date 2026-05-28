"""
Question:
Swap keys and values in a dictionary.
"""

# Write your code here

data = {"a": 1, "b": 2, "c": 3}

swapped = {value: key for key,value in 
           data.items() }

print(swapped)