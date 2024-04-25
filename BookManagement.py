class Book:
    def __init__(self, id, title, author, genre, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.borrowed = 0
        self.status = "Available"

class BooksManager:
    def __init__(self):
        self.book_list = dict()
        self.borrowed_book = list()

    def add_book(self, book):
        self.book_list[book.id] = [book.title, book.author, book.genre, book.quantity, book.borrowed, book.status]
        print("Book added successfully!")

    def change_info(self):
        change = input("Enter book's id to change info: ")
        if change in self.book_list:
            num = int(input("Choose the number of category you want to change: 1.title  |  2.author  |  3.genre  |  4.quantity \n"))
            if 0 < num < 5:
                new = input("Enter new info: ")
                self.book_list[change][num - 1] = new.title()
                print("Book info changed!")
            else:
                print("Invalid number. Please try again!")
        else:
            print("Book no found.")

    def remove_book(self):
        remove = input("Enter book's id to remove: ")
        try:
            self.book_list.pop(remove)
            print("Book removed!")
        except KeyError:
            print("This book does not exist!")

    def find_book(self):
        book = input("Enter book's id to find: ")
        if book in self.book_list:
            print_table()
            print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|{self.book_list[book][2].center(15)}|"
                  f"{str(self.book_list[book][3]).center(15)}|{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
            print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
        else:
            print("Book not found.")

    def display_book_list(self):
        if not self.book_list:
            print("There is no book to display.")
        else:
            print_table()
            for book in sorted(self.book_list):
                print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                      f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                      f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
                print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")

    def sort_book_list(self):  # Sort book title
        if not self.book_list:
            print("There is no book to sort.")
        else:
            print_table()
            for book, value in sorted(self.book_list.items(), key=lambda info: info[1][0]):
                print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                      f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                      f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
                print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")

    def filter(self):
        if not self.book_list:
            print("There is no book to filter.")
        else:
            category = int(
                input("Choose a number of category to filter: 1.title  |  2.author  |  3.genre  |  4.status \n"))
            if 0 < category < 5:
                if category == 4:
                    category += 2  # change index to Status
                    value = input("Enter a value to filter out:  Available  |  Not Available \n")
                else:
                    value = input("Enter the value to filter out: ")
                print_table()
                for book in self.book_list:
                    if self.book_list[book][category - 1] == value.title():
                        print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                              f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                              f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
                        print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
            else:
                print("Invalid number. Please try again!")

    def borrow_book(self, id):
        if self.book_list[id][5] == "Available":
            self.borrowed_book.append(id)
            self.book_list[id][4] += 1
            print("Borrowed book successfully!")
        else:
            print("This book is not available now!")
        if self.book_list[id][3] == self.book_list[id][4]:
            self.book_list[id][5] = "Not Available"

    def return_book(self, id):
        try:
            self.borrowed_book.remove(id)
            self.book_list[id][4] -= 1
            print("Returned book successfully!")
            if self.book_list[id][4] < self.book_list[id][3]:
                self.book_list[id][5] = "Available"
        except:
            print("This book was not borrowed.")

    def print_borrowed_list(self):
        if not self.borrowed_book:
            print("There is no borrowed book to display.")
        else:
            print("+------------------------------+")
            print("|        Borrowed Books        |")
            print("+--------+---------------------+")
            print("|  ID    |        Title        |")
            print("+--------+---------------------+")
            for book in self.borrowed_book:
                print(f'|{book.center(8)}|{self.book_list[book][0].center(21)}|')
                print("+--------+---------------------+")

    def save_file_borrowed_book(self):
        if not self.borrowed_book:
            print("There is no data to save.")
        else:
            data = open("Borrowed_books.txt", "w")
            data.write("+------------------------------+\n")
            data.write("|        Borrowed Books        |\n")
            data.write("+--------+---------------------+\n")
            data.write("|  ID    |        Title        |\n")
            data.write("+--------+---------------------+\n")
            for book in self.borrowed_book:
                data.write(f'|{book.center(8)}|{self.book_list[book][0].center(21)}|\n')
                data.write("+--------+---------------------+\n")

    def save_file_book_list(self):
        if not self.book_list:
            print("There is no book data to save.")
        else:
            data = open("Book_list.txt", "w")
            data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
            data.write("|  ID    |        Title        |       Author       |     Genre     |   Quantity    |   Borrowed    |    Status     |\n")
            data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
            for book in sorted(self.book_list):
                data.write(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                           f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                           f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|\n")
                data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
            print("Saved to file!")
            data.close()

    def check_id(self, id):
        if id in self.book_list:
            return 1
        else:
            return 0

def print_table():
    print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
    print("|  ID    |        Title        |       Author       |     Genre     |   Quantity    |   Borrowed    |    Status     |")
    print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
