"""
Question:
Replace negative numbers with 0 after conversion.
"""

# Write your code here

t = (1,-2,3,-4)

l = list(t)

for i in range(len(l)):
    if l[i] < 0:
        l[i] = 0

t = tuple(l)

print(l)