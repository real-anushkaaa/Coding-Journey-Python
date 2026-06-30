"""
Python map(), filter(), and reduce() Practice

Question:
Convert a list of integers into strings.

# Note:
# Import reduce using:
# from functools import reduce
"""

# Write your solution below.

l = [10,20,30,40]
new = list(map(str, l))
print(new)