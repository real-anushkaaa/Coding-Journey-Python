# Create a password checker that stops when correct password is entered. 

correct_password = "admin123"

while True:
    password = input("enter the password : ")

    if password == correct_password:
        print("password is correct")
        break

    else:
        print("incorrect password")