"""
Question:
Find key having maximum value.
"""

# Write your code here

marks = {"Math": 80, "Science": 95, "English": 85}

max_key = max(marks, key=marks.get)

print(max_key)