# Take a number and check whether it is a 3-digit number or not.

num = int(input("enter the number"))

if 100 <= num <= 999:
    print("3-digit number")
else:
    print("Not 3-digit")