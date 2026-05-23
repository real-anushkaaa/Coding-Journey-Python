# ----------------------------------------
# Create nested lambda function.
# ----------------------------------------


multiply = lambda x : (lambda y : x*y)

result = multiply(5)
print(result(4))