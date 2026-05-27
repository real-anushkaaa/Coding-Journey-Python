"""
Question:
Reverse all strings inside a tuple.
"""

# Write your code here

t = ("hello","python","world")

result = ()

for i in t:
    result = result + (i[::-1])

print(result)