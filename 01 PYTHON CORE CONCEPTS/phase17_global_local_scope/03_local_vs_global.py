# Question 3
# Create a global variable a = 5 and a local variable a = 20 inside a function. Print both values.

a = 5

def my_func():
    a = 20
    print(a)

my_func()
print(a)