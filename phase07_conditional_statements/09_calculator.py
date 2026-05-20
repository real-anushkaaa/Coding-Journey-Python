# Take two numbers and perform operation based on user choice:
# (+, -, *, /)

a = int(input("enter the number"))
b = int(input("enter the number"))
op = input("enter the operator")

if op == '+':
    print(a+b)

elif op == '-':
    print(a-b)

elif op == '/':
    print(a/b)

elif op == '*':
    print(a*b)

else:
    print("invalid operator")