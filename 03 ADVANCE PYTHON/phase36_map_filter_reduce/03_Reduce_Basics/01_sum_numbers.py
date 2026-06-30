"""
Python map(), filter(), and reduce() Practice

Question:
Find the sum of all numbers.

# Note:
# Import reduce using:
# from functools import reduce
"""

# Write your solution below.

from functools import reduce

numbers = [10,20,30,10,20,10]
new = (reduce(lambda a,b : a + b , numbers))
print(new)
