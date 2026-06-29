# Find product of numbers from 1 to n. 

n = int(input("enter the number"))
product = 1
i = 1

while i<=n:
    product*=i
    i+=1
print(product)