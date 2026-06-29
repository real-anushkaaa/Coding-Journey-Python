"""
Question:
Find unique vowels from a string using set.
"""

# Write your code here

text = "programming"

vowels = {'a','e','i','o','u'}

result = set()

for ch in text:
    if ch in vowels:
        result.add(ch)

print(result)