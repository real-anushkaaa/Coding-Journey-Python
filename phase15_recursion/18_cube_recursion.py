# Find cube of a number using recursion

def cube(n):

    if n == 0:
        return 0

    return cube(n - 1) + 3 * n * n - 3 * n + 1


print(cube(3))