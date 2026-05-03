# Take a year as input and check whether it is a leap year.

year = int(input("enter the number"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")

else:
    print("not a leap year")
    