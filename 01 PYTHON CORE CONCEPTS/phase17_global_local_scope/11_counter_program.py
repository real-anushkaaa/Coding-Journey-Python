# Question 11
# Create a global counter variable and update it every time a function is called.

counter = 0

def my_func():
    global counter
    counter += 1
    print(counter)

my_func()
my_func()
my_func()
my_func()