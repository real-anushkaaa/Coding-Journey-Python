# --------------------------------------------------
# Create function to calculate discount.
# --------------------------------------------------

def discount(price):
    final_price = price - (price * 20 / 100)
    print("discount : ", final_price)

discount(1000)