library = []

while True:
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.append(book)
        print(book, "added successfully!")

    elif choice == 2:
        if len(library) == 0:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i in range(len(library)):
                print(i + 1, ".", library[i])

    elif choice == 3:
        search = input("Enter book name to search: ")
        if search in library:
            print(search, "is available in library.")
        else:
            print(search, "not found.")

    elif choice == 4:
        issue = input("Enter book name to issue: ")
        if issue in library:
            library.remove(issue)
            print(issue, "issued successfully.")
        else:
            print("Book not available.")

    elif choice == 5:
        book = input("Enter book name to return: ")
        library.append(book)
        print(book, "returned successfully.")

    elif choice == 6:
        delete = input("Enter book name to delete: ")
        if delete in library:
            library.remove(delete)
            print(delete, "deleted successfully.")
        else:
            print("Book not found.")

    elif choice == 7:
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")