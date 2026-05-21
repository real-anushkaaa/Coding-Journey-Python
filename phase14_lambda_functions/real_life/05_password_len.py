# ----------------------------------------
# Create lambda to check password length.
# ----------------------------------------

check_password = lambda password: "strong pass" if len(password)>=10 else "weak"

print(check_password("anuskavaran"))