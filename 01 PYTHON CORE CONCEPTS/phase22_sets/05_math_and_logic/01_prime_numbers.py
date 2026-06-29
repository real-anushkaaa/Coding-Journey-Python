"""
Question:
Find all prime numbers in a set.
"""

# Write your code here

numbers = {2, 3, 4, 5, 6, 7, 8, 11}

for num in numbers:
    if num > 1:
        prime = True

        for i in range(2,num):
            if num % i == 0:
                prime = False
                break
            
        if prime:
            print(num)