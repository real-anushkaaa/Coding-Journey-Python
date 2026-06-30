"""
Python map(), filter(), and reduce() Practice

Question:
Use map() to square every number.

# Note:
# Import reduce using:
# from functools import reduce
"""

# Write your solution below.

number = [2,4,6,8,10]

new = list(map(lambda x: x * x , number))
print(new)