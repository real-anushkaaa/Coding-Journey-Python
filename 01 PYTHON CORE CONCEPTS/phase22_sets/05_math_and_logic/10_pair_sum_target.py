"""
Question:
Find pair of elements whose sum equals a target value.
"""

# Write your code here

numbers = {2, 4, 6, 8, 10}
target = 12

for num in numbers:
    if target - num in numbers and num < target-num:
        print(num,target-num)

        