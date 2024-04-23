class Book:
    def __init__(self, id, title, author, genre, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.borrowed = 0
        self.status = "Available"

    def borrowed_book(self):
        if self.borrowed != self.quantity:
            self.borrowed += 1
        if self.borrowed == self.quantity:
            self.status = "Not Available"

class BooksManager:
    def __init__(self):
        self.book_list = dict()

    def add_book(self, book):
        self.book_list[book.id] = [book.title, book.author, book.genre, book.quantity, book.borrowed, book.status]
        print("Book added successfully!")

    def change_info(self):
        change = input("Enter book's id to change info: ")
        if change in self.book_list:
            num = int(input(
                "Choose the number of category you want to change: 1.title  |  2.author  |  3.genre  |  4.quantity \n"))
            if 0 < num < 5:
                new = input("Enter new info: ")
                self.book_list[change][num - 1] = new.title()
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
            print(f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}  Borrowed: {self.book_list[book][4]}")
        except KeyError:
            print("Book not found")

    def display_book_list(self):
        for book in sorted(self.book_list):
            print(f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}  Borrowed: {self.book_list[book][4]}")

    def sort_book_list(self):
        for book, value in sorted(self.book_list.items(), key=lambda info: info[1][0]):
            print(f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}  Borrowed: {self.book_list[book][4]}")

    def filter(self):
        category = int(input("Choose a number of category to filter: 1.title  |  2.author  |  3.genre  |  4.status \n"))
        if 0 < category < 4:
            value = input("Enter the value to filter out: ")
            for book in self.book_list:
                if self.book_list[book][category - 1] == value.title():
                    print(f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}  Borrowed: {self.book_list[book][4]}")
        elif category == 4:
            status = input("Choose the status to filter out:  Available  |  Not Available \n")
            for book, value in self.book_list.items():
                if value[5] == status.title():
                    print(f"{value[5]}  ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}  Borrowed: {self.book_list[book][4]}")
        else:
            print("Please choose a number between 1 and 4. Try again!")

    def save_file(self):
        data = open("Book_list.txt", "w")
        for book in sorted(self.book_list):
            data.write(f"ID: {book}  Title: {self.book_list[book][0]}  Author: {self.book_list[book][1]}  Genre: {self.book_list[book][2]}  Number of copy: {self.book_list[book][3]}  Borrowed: {self.book_list[book][4]}  Status: {self.book_list[book][5]}\n")
        print("Saved to file!")
        data.close()

    def check_id(self, id):
        if id in self.book_list:
            return 1
        else:
            return 0
