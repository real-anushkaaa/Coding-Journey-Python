# --------------------------------------------------
# Create function to calculate salary bonus.
# --------------------------------------------------

def bonus(salary):
    total = salary + (salary * 10 / 100)
    print("salary bonus : ", total)

bonus(50000)