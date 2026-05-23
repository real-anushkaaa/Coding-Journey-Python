# ----------------------------------------
# Create lambda for tax calculation.
# ----------------------------------------

tax = lambda amount : amount + (amount * 18 / 100)

print(tax(5000))