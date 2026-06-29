# --------------------------------------------------
# Create calculator using functions.
# --------------------------------------------------

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    
    return "cacnot divided by zero"

print(add(10, 5))
print(sub(10, 5))
print(multi(10, 5))
print(div(10, 5))
