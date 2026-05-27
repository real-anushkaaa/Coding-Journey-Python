"""
Question:
Flatten a nested tuple.
"""

# Write your code here

t = ((1, 2), (3, 4), (5, 6))

result = ()

for i in t:
    result = result + i

print(result)