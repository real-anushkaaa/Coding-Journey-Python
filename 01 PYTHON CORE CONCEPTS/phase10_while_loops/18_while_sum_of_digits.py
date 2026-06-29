# Find sum of digits of a number. 

n = int(input("enter the number : "))
total = 0 

while n != 0:
    digit = n % 10
    total += digit
    n //= 10
print(total)