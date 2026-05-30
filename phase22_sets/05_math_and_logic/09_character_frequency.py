"""
Question:
Count frequency of characters using set and loops.
"""

# Write your code here

text = "banana"

for ch in set(text):
    count = 0

    for c in text:
        if ch == c:
            count+=1

    print(ch,":", count)

