"""
Question:
Find the largest and second largest element.
"""

# Write your code here

t = (10,20,30,40)

largest = max(t)

temp = list(t)
temp.remove(largest)

second_largest = max(temp)

print("tuple : ",t)
print("largest : ", largest)
print("second_largest : ", second_largest)