"""
Question:
Count occurrences of elements in a list using dictionary.
"""

# Write your code here

numbers = [1, 2, 1, 3, 2, 1]

count_dict = {}

for num in numbers:
    count_dict[num] = count_dict.get(num, 0)
    + 1

print(count_dict)
