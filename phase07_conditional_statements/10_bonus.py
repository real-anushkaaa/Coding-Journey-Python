# Take salary as input and calculate bonus:
# 50000 → 10% bonus
# Otherwise → 5% bonus

salary = int(input("enter the salary"))

if salary > 50000:
    print(salary * 0.10)
else:
    print(salary * 0.05)