"""
Python map(), filter(), and reduce() Practice

Question:
Use map() to double every number in a list.

# Note:
# Import reduce using:
# from functools import reduce
"""

# Write your solution below.

number = [2,4,6,8,10]

new = list(map(lambda x: x * 2 , number))
print(new)