# Question 7
# Use one global variable in two different functions.

x = 10

def my_func1():
    print(x)

def my_func2():
    print(x)

my_func1()
my_func2()
