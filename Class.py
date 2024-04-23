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
            print("This book does not exist!")

    def find_book(self):
        book = input("Enter book's id to find: ")
        if book in self.book_list:
            print_table()
            print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|{self.book_list[book][2].center(15)}|"
                  f"{str(self.book_list[book][3]).center(15)}|{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
            print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
        else:
            print("Book not found")

    def display_book_list(self):
        print_table()
        for book in sorted(self.book_list):
            print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|{self.book_list[book][2].center(15)}|"
                  f"{str(self.book_list[book][3]).center(15)}|{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
            print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")

    def sort_book_list(self):  # Sort book title
        print_table()
        for book, value in sorted(self.book_list.items(), key=lambda info: info[1][0]):
            print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|{self.book_list[book][2].center(15)}|"
                  f"{str(self.book_list[book][3]).center(15)}|{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
            print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")

    def filter(self):
        category = int(input("Choose a number of category to filter: 1.title  |  2.author  |  3.genre  |  4.status \n"))
        if 0 < category < 5:
            if category == 4:
                category += 2  # change index to Status
                value = input("Enter a value to filter out:  Available  |  Not Available \n")
            else:
                value = input("Enter the value to filter out: ")
            print_table()
            for book in self.book_list:
                if self.book_list[book][category - 1] == value.title():
                    print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|{self.book_list[book][2].center(15)}|"
                          f"{str(self.book_list[book][3]).center(15)}|{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
                    print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
        else:
            print("Please choose a number between 1 and 5. Try again!")

    def save_file(self):
        data = open("Book_list.txt", "w")
        data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
        data.write("|  ID    |        Title        |       Author       |     Genre     |   Quantity    |   Borrowed    |    Status     |\n")
        data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
        for book in sorted(self.book_list):
            data.write(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|{self.book_list[book][2].center(15)}|"
                       f"{str(self.book_list[book][3]).center(15)}|{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|\n")
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
