# Take username and password as input and check if login is successful 
# or failed (use predefined values).

username = input("enter the username")
password = input("enter the password")

if username == "admin" and password == "12345":
    print("successful")

else:
    print("failed")