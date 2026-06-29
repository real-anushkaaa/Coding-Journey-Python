# --------------------------------------------------
# Create function to check voting eligibility.
# --------------------------------------------------

def voting_age(age):
    if age >= 18:
        print("eligible")

    else:
        print("not eligible")

voting_age(20)