# Check whether duplicates exist.

list = [1, 2, 3, 2]

if len(list) != len(set(list)):
    print("duplicates exist")

else:
    print("duplicates")

