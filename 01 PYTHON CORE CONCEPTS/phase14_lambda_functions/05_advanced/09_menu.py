# ----------------------------------------
# Create menu-driven program using lambda.
# ----------------------------------------

operations = {
    1 : lambda a,b : a+b,
    2 : lambda a,b : a-b,
    3 : lambda a,b : a/b,
    4 : lambda a,b : a*b,
}

choice = int(input("1.Add 2.Subtract 3.Multiply 4.Divide : "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("result : ", operations[choice](a,b))