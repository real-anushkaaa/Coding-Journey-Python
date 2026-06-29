"""
Question:
Find the smallest and second smallest element.
"""

# Write your code here

t = (10,20,30,40)

smallest = min(t)

temp = list(t)
temp.remove(smallest)

second = min(temp)

print("tuple : ",t)
print("smallest : ", smallest)
print("second : ", second)