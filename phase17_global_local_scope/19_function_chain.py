# Question 19
# Use one global variable across three functions where each function changes its value.

value = 10

def first():

    global value

    value += 5

def second():

    global value

    value *= 2

def third():

    global value

    value -= 3

first()
second()
third()

print(value)