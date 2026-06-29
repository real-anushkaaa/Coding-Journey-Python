# Print 1 to n using recursion

def print_number(n):
    if n == 0:
        return 
    
    print_number(n-1)
    print(n)

print_number(10)