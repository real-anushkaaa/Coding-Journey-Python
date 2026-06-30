"""
Python map(), filter(), and reduce() Practice

Question:
Find the product of all numbers.

# Note:
# Import reduce using:
# from functools import reduce
"""

# Write your solution below.

from functools import reduce

numbers = [2,3,4,5]
new = reduce(lambda a,b: a*b, numbers)
print(new)