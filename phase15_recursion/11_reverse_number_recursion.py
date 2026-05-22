# Reverse a number

def reverse_number(n, reverse = 0):
    if n == 0:
        return reverse
    
    digit = n % 10

    reverse = reverse * 10 + digit

    return reverse_number(n // 10, reverse)

print(reverse_number(1234))