# Print numbers between 1 to n that are odd.

n = int(input("enter the number"))

for i in range(1, n+1):
    if i % 2 != 0:
        print(i)