# Question 6
# Create a global variable count = 0. Increase its value inside a function using the global keyword.

count = 0

def my_func():
    global count
    count += 1

my_func()
print(count)