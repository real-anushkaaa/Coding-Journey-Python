# check if a number is divisible by 3 OR 5.

num = int(input("enter the number"))

if num % 3 == 0 or num % 5 == 0:
    print("Divisible by 3 or 5")
else:
    print("Not divisible")