# Take a number and check whether it is divisible by both 3 and 5.

a = int(input("enter the number"))

if a % 3 == 0 and a % 5 == 0:
    print("divisible by 3 and 5")

else:
    print("not divisiable by 3 and 5 ")