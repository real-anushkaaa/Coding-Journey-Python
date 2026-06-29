"""
Question:
Find key having minimum value.
"""

# Write your code here

marks = {"Math": 80, "Science": 95, "English": 85}

min_key = min(marks, key = marks.get)

print(min_key)