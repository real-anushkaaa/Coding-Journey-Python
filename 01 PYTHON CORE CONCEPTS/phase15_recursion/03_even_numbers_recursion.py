# Print even numbers from 1 to n

def even(n):
    if n == 0:
        return
    
    even(n-1)

    if n % 2 == 0:
        print(n)


even(20)