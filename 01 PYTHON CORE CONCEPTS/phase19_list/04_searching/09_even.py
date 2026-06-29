# Count even numbers in list.

list = [2,4,3,10,20]
count = 0

for i in list:
    if i % 2 == 0:
        count+=1

print(count)