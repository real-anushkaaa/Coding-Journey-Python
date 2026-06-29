# Take password input and check minimum length.

password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password")

else:
    print("Password too short")