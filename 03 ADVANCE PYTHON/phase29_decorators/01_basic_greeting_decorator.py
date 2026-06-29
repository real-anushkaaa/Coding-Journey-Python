"""
Python Decorators Practice

Question:
Create a decorator greet_decorator that prints 'Before function execution', 
executes the decorated function, and then prints 'After function execution'. 
Apply it to a function say_hello().
"""

# Write your solution below.

def greet_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@greet_decorator
def say_hello():
    print("hello")

say_hello()