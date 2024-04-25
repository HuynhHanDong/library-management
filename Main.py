from BookManagement import*

def main():
    while True:
        print("\n+------------ Library Management System ------------+")
        print("|                                                   |")
        print("|  Which Section Would You Like To Manage?          |")
        print("|  1. Book Management                               |")
        print("|  2. Reader Management                             |")
        print("|  3. Exit                                          |")
        print("|                                                   |")
        print("+---------------------------------------------------+")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                print("Moving to Book Management Section...")
                book_menu()
            elif choice == 2:
                print("Moving to Reader Management Section...")
                pass
            elif choice == 3:
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again!")
        except:
            print("Invalid input. Please try again!")
        print()
        print("~" * 120)

def book_menu():
    manager = BooksManager()
    while True:
        print("\n+----------------- Book Management -----------------+")
        print("|  1. Add Book                                      |")
        print("|  2. Change Book Info                              |")
        print("|  3. Remove Book                                   |")
        print("|  4. Find Book                                     |")
        print("|  5. Display All Books                             |")
        print("|  6. Sort Book list By Alphabetical Title          |")
        print("|  7. Display Book List With filter                 |")
        print("|  8. Save Data To File                             |")
        print("|  9. Exit                                          |")
        print("+---------------------------------------------------+")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                id = input("Enter book's id: ")
                if manager.check_id(id):
                    print("This ID is already existed. Please try again!")
                    continue
                title = input("Enter book's title: ")
                title = title.title()
                author = input("Enter book's author: ")
                author = author.title()
                genre = input("Enter book's genre: ")
                genre = genre.title()
                quantity = int(input("Enter number of copies: "))
                if quantity <= 0:
                    print("Number of copies must be larger than 0. Please try again!")
                    continue
                book = Book(id, title, author, genre, quantity)
                manager.add_book(book)

            elif choice == 2:
                manager.change_info()

            elif choice == 3:
                manager.remove_book()

            elif choice == 4:
                manager.find_book()

            elif choice == 5:
                manager.display_book_list()

            elif choice == 6:
                manager.sort_book_list()

            elif choice == 7:
                manager.filter()

            elif choice == 8:
                manager.print_borrowed_list()

            elif choice == 9:
                manager.save_file_borrowed_book()

            elif choice == 10:
                manager.save_file_book_list()

            elif choice == 11:
                print("Exiting Book Management Section...")
                break

            else:
                print("Invalid choice. Please try again.")
        except:
            print("Invalid input. Please try again.")
        print()
        print("~" * 120)

if __name__ == "__main__":
    main()
