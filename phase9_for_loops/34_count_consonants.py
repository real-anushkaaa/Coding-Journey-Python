# Count consonants in a string.

s = input("enter the string")
count = 0
vowels = "aeiou"

for ch in s:
    if ch not in vowels:
        count += 1
        print(count)