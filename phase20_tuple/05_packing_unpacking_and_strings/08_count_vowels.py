"""
Question:
Count vowels in tuple strings.
"""

# Write your code here

t = ("apple", "orange", "sky")

count = 0

for word in t:
    for ch in word:
        if ch.lower() in "aeiou":
            count += 1

print(count)