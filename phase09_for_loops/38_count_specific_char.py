# Count occurrence of a specific character.

s = input("enter the string : ")
target = input("enter the target : ")
count = 0

for ch in s:
    if ch == target:
        count += 1

print(count)