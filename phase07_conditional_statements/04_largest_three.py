# Take three numbers and find the largest among them.

a = int(input("enter the number: "))
b = int(input("enter the number: "))
c = int(input("enter the number: "))

if a >= b and a>=c:
    print("a is greater")

elif b >= c:
    print("b is greater")

else:
    print("c is greater")