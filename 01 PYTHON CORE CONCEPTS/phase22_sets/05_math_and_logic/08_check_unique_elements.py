"""
Question:
Check whether all elements are unique in a list.
"""

# Write your code here

numbers = [1, 2, 3, 4, 5]

if len(numbers) == len(set(numbers)):
    print("All elements are unique")
else:
    print("Duplicates found")