# Check palindrome number

def reverse_number(n, rev = 0):

    if n == 0:
        return rev
    
    return reverse_number(n // 10, rev * 10 + n % 10)

n = 121

if n == reverse_number(n):
    print("palindrome")

else:
    print("not palindrome")