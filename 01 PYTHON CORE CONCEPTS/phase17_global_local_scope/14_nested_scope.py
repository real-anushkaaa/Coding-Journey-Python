# Question 14
# Create a function inside another function and access variables from the outer function.

def outer():
    message = "hello"

    def inner():
        print(message)

    inner()

outer()