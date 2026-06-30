"""
Python map(), filter(), and reduce() Practice

Question:
Filter all odd numbers.

# Note:
# Import reduce using:
# from functools import reduce
"""

# Write your solution below.

number = [1,2,3,4,5,6,7,8,9,10]
new = list(filter(lambda x: x % 2 != 0 , number))
print(new)