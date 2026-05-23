# Print numbers from 1 to 100 and stop at first number divisible by 17. 

for i in range(1,101):
    if i % 17 == 0:
        print(i)
        break
    