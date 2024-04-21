class Book:
    def __init__(self, id, title, author, genre, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity


class BooksManagement:
    def __init__(self):
        self.book_list = dict()

    def add_book(self, book):
        self.book_list[book.id] = [book.title, book.author, book.genre, book.quantity]
        print("Book added successfully!")

    def change_info(self):
        change = input("Enter book's id to change info: ")
        if change in self.book_list:
            num = int(input(
                "Choose the number of category you want to change: 1.title  |  2.author  |  3.genre  |  4.quantity \n"))
            if 0 < num < 5:
                new = input("Enter new info: ")
                self.book_list[change][num - 1] = new
                print("Book info changed!")
            else:
                print("Please choose a number between 1 and 4. Try again!")
        else:
            print("Book no found")

    def remove_book(self):
        remove = input("Enter book's id to remove: ")
        try:
            self.book_list.pop(remove)
            print("Book removed!")
        except KeyError:
            print("Book not found!")

    def find_book(self):  # find book by category
        book = input("Enter book's id to find: ")
        try:
            print(
                f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}")
        except KeyError:
            print("Book not found")

    def sort_book_list(self):
        for key, value in sorted(self.book_list.items(), key=lambda info: info[1][0]):
            print(
                f"ID: {key}  Title: {self.book_list[key][0]}  Author: {self.book_list[key][1]}  Genre: {self.book_list[key][2]}  Number of copy: {self.book_list[key][3]}")

    def display_book_list(self):
        for book in sorted(self.book_list):
            print(
                f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}")

    def filter(self):
        category = int(input("Choose a number of category to filter: 1.title  |  2.author  |  3.genre \n"))
        if 0 < category < 4:
            value = input("Enter the value to filter out: ")
            for book in self.book_list:
                if self.book_list[book][category - 1] == value:
                    print(
                        f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}")
        else:
            print("Please choose a number between 1 and 3. Try again!")

    def save_file(self):
        data = open("Book_list.txt", "w")
        for book in sorted(self.book_list):
            data.write(
                f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]} \n")
        print("Saved to file!")
        data.close()

    def check_id(self, id):
        if id in self.book_list:
            return 1
        else:
            return 0


def main():
    manager = BooksManagement()

    while True:
        print("\n---------- Student Management System ----------")
        print("1. Add Book")
        print("2. Change Book Info")
        print("3. Remove Book")
        print("4. Find Book")
        print("5. Display All Books")
        print("6. Print Book list By Alphabetical Title")
        print("7. Display Book List With filter")
        print("8. Save Data To File")
        print("9. Exit")
        print("-" * 50)

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                id = input("Enter book's id: ")
                if manager.check_id(id):
                    print("This ID is already existed.")
                    continue
                title = input("Enter book's title: ")
                author = input("Enter book's author: ")
                genre = input("Enter book's genre: ")
                quantity = int(input("Enter number of copies: "))
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
                manager.save_file()

            elif choice == 9:
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")
        except:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
