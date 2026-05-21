# --------------------------------------------------
# Create ATM menu using functions.
# --------------------------------------------------

balance = 10000

def check_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount
    print("updated balance : ", balance)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("remaining balance : ", balance)

    else:
        print("insuffincient balance")

check_balance()
deposit(2000)
withdraw(500)