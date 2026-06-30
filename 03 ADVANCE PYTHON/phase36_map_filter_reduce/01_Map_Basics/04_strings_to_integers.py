"""
Python map(), filter(), and reduce() Practice

Question:
Convert a list of strings into integers using map().

# Note:
# Import reduce using:
# from functools import reduce
"""

# Write your solution below.

l = ['10','20','30','40']
new = list(map(int, l))
print(new)