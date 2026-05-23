# Question 20
# Create:
# - One global variable
# - One local variable
# - One nested function
# Print all variables correctly according to scope rules.

global_var = "Global"

def outer():

    local_var = "Local"

    def inner():

        nested_var = "Nested"

        print(global_var)
        print(local_var)
        print(nested_var)

    inner()

outer()
