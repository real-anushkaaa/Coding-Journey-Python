# ----------------------------------------
# Create lambda for discount calculation.
# ----------------------------------------

discount = lambda price : price - (price * 20 / 100)

print(discount(1000))