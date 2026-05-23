# Search for a number in a list and stop loop when found.

numbers = [10,20,30,40,50]
target = 30

for num in numbers:
    if num == target:
        print("number found")
        break