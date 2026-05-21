# Print sum of odd numbers from 1 to 50.

total = 0

for i in range(1,51):
    if i % 2 != 0:
        total+=i

print(total)