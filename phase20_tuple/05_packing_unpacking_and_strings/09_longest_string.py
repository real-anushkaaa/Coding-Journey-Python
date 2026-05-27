"""
Question:
Find the longest string in a tuple.
"""

# Write your code here

t = ("cat", "elephant", "dog")

longest = max(t, key=len)

print(longest)