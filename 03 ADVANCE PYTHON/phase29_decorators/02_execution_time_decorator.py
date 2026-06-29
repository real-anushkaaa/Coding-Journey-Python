"""
Python Decorators Practice

Question:
Create a decorator calculate_time that measures and prints the execution time of a function.
Apply it to a function that prints numbers from 1 to 100000.
"""

# Write your solution below.

import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start, "seconds")
    return wrapper

@calculate_time
def print_numbers():
    for i in range(1,100000):
        print(i)

print_numbers()


    