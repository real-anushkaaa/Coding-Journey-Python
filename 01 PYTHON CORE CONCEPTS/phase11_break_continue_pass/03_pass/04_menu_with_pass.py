# Create a menu program where one option is not implemented yet using pass. 

while True:
    print("\n1. Start")
    print("2. Settings")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Program Started")

    elif choice == 2:
        pass

    elif choice == 3:
        break

    else:
        print("Invalid Choice")