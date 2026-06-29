# --------------------------------------------------
# Create bill generator function.
# --------------------------------------------------


def generate_bill(item, price, quantity):

    total = price * quantity

    print("Item:", item)
    print("Quantity:", quantity)
    print("Total Bill =", total)

generate_bill("Book", 200, 3)
