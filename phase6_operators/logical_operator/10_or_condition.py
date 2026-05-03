# Take two conditions and combine using or.

a = int(input("enter the number"))
b = int(input("enter the number"))

if a > 10 or b > 10:
    print("At least one is greater than 10")
else:
    print("Condition failed")