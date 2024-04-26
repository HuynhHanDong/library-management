from BookManagement import*
from ReaderManagement import *
from CirculationManager import CirculationManager

def main():
    while True:
        print("\n+------------ Library Management System ------------+")
        print("|                                                   |")
        print("|  Which Section Would You Like To Manage?          |")
        print("|  1. Book Management                               |")
        print("|  2. Reader Management                             |")
        print("|  3. Circulation Manager                           |")
        print("|  4. Exit                                          |")
        print("+---------------------------------------------------+")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                print("Moving to Book Management Section...")
                book_menu()
            elif choice == 2:
                print("Moving to Reader Management Section...")
                reader_menu()
            elif choice == 3:
                print("Moving to Circulation Manager Section...")
                manager_menu()
            elif choice == 4:
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
        print("|  8. Print Borrowed Book List                      |")
        print("|  9. Save File Borrowed Book                       |")
        print("|  10. Save File Book List                          |")
        print("|  11. Exit                                         |")
        print("+---------------------------------------------------+")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                id = input("Enter book's id: ")
                if manager.check_id(id):
                    print("This ID is already existed. Please try again!")
                    continue
                title = input("Enter book's title: ")
                author = input("Enter book's author: ")
                genre = input("Enter book's genre: ")
                quantity = int(input("Enter book quantity: "))
                if quantity <= 0:
                    print("Number of copies must be larger than 0. Please try again!")
                    continue
                book = Book(id, title.title(), author.title(), genre.title(), quantity)
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

def reader_menu():
    reader_management = ReaderManagement()
    while True:
        print("\n+--------------------- Readers management ----------------------+")
        print("|  1. Add reader                                                |")
        print("|  2. Change reader info                                        |")
        print("|  3. Remove reader                                             |")
        print("|  4. Find reader by name                                       |")
        print("|  5. Display list of reader                                    |")
        print("|  6. Print list of reader with descending borrow date / fine   |")
        print("|  7. Show list of reader with filter                           |")
        print("|  8. Return book                                               |")
        print("|  9. Save to file                                              |")
        print("|  10. Exit                                                     |")
        print("+---------------------------------------------------------------+")

        try:
            action = int(input("Enter your action: "))
            if action == 1:
                name = input("Enter reader's name: ")
                email = input("Enter reader's email: ")
                phone_number = int(input("Enter reader's phone number: "))
                title_of_book = input("Enter title of borrowed book: ")
                borrow_date = input("Enter borrow date, format is year-month-day: ")
                new_reader = Reader(name.title(), email.lower(), phone_number, title_of_book.title(), borrow_date)
                reader_management.add_reader(new_reader)

            elif action == 2:
                reader_management.change_reader_info()

            elif action == 3:
                reader_management.remove_reader()

            elif action == 4:
                found = reader_management.find_reader_by_name()
                if not found:
                    print("Reader does not exist.")

            elif action == 5:
                reader_management.display_list_of_readers()

            elif action == 6:
                reader_management.print_list_by_borrow_date_or_fine()

            elif action == 7:
                user_input = input("Enter filter_key-filter_value pairs (e.g., name:Sang, email:Sang@): ")
                pairs = user_input.split(',')
                key_value_pairs = [pair.strip().split(':') for pair in pairs]
                arguments = {key.strip(): value.strip() for key, value in key_value_pairs}
                reader_management.show_list_of_readers_with_filter(**arguments)

            elif action == 8:
                returned = reader_management.add_returned_book()
                if not returned:
                    print("Invalid book title. Please try again!")

            elif action == 9:
                reader_management.save_to_file()

            elif action == 10:
                print("Exiting Readers Management...")
                break

            else:
                print("Invalid choice. Please try again.")

        except:
            print("Invalid input. Please try again.")

def manager_menu():
    circulation_manager = CirculationManager()
    while True:
        print("Circulation Manager:")
        print("1. ...")
        print("2. ...")
        print("3. Send a Fine")
        print("4. Exit")

        action = input("Enter your action: ")
        if action == "4":
            break
        elif action == "1":
            pass
        elif action == "2":
            pass
        elif action == "3":
            pass
            #circulation_manager.check_return_dates(reader_management=reader_management)
if __name__ == "__main__":
    main()
