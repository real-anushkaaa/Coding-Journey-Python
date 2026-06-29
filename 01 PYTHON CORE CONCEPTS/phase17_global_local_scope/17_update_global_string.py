# Question 17
# Create a global string and modify it inside a function using global.

text = "anushka varan"

def my_func():
    global text
    
    text = "aditya"

my_func()
print(text)