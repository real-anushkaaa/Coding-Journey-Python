"""
Question:
Find frequency of characters in a string using dictionary.
"""

# Write your code here

text = "hello"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1