# Question 10
# Create both local and global variables with the same name and check which one Python uses inside the function.

x = 10

def my_func():
    x = 200
    print(x)

my_func()
print(x)
