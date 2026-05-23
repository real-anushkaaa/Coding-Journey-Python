# Check if a number is divisible by 2 AND 3.

num = int(input("enter the number"))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by 2 and 3")
else:
    print("Not divisible by both")