# Question 12
# Create a global list and append elements inside a function.

list = [10,20,30,40,50]

def my_func():
    global list
    list.append(60)
    list.append(70)
    list.append(80)

my_func()
print(list)