# --------------------------------------------------
# Create login validation function.
# --------------------------------------------------

def login(username,password):
    if username == "admin" and password == "1234":
        print("login successful")

    else:
        print("invalid username+password")

login("admin","1234")