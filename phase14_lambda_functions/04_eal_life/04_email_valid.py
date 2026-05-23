# ----------------------------------------
# Create lambda for email validation.
# ----------------------------------------

validate = lambda email: "valid" if "@" in email and "." in email else "invalid"

print(validate("vannu.9204@gmail.com"))