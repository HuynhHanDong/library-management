from datetime import datetime, timedelta

class Reader:
    def __init__(self, name, email, phone_number, book_title, borrow_date, status='False', fine=0):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.book_title = book_title
        self.borrow_date = datetime.strptime(borrow_date, '%Y-%m-%d')
        self.expired_date = self.borrow_date + timedelta(days=30)
        self.status = status
        self.fine = fine

    def display_info(self):
        print(f"| {self.name} | {self.email} | {self.phone_number} | {self.book_title} | {self.borrow_date.strftime('%Y-%m-%d')} | "
              f"{self.expired_date.strftime('%Y-%m-%d')} | {self.status} | {self.fine} |")

class ReaderManagement:
    def __init__(self):
        self.readers = []

    def add_reader(self, new_reader):
        self.readers.append(new_reader)
        print(f"Added new reader successfully!")

    def change_reader_info(self):
        name = input("Enter the name of the reader needed to change info: ")
        if self.check_reader(name):
            change = input("Enter the category you want to change: Name  |  Email  | Phone number \n")
            new = input("Enter new info: ")
            for reader in self.readers:
                if reader.name == name.title():
                    if change.lower() == 'name':
                        reader.name = new.title()
                        print("Reader information updated successfully.")
                    elif change.lower() == 'email':
                        reader.email = new.lower()
                        print("Reader information updated successfully.")
                    elif change.lower() == 'phone number':
                        reader.phone_number = int(new)
                        print("Reader information updated successfully.")
        else:
            print("Reader not found.")

    def remove_reader(self):
        name = input("Enter name of the reader to remove: ")
        if self.check_reader(name.title()):
            book = input(f"Enter title of book {name.title()} borrowed: ")
            for i, reader in enumerate(self.readers):
                if reader.name == name.title() and reader.book_title == book.title():
                    del self.readers[i]
                    print("Reader removed successfully.")
        else: 
            print("Reader not found.")
            
    def find_reader_by_name(self):
        found = False
        name = input("Enter the name of the reader to find: ")
        for reader in self.readers:
            if reader.name == name.title():
                reader.display_info()
                found = True
        return found

    def display_list_of_readers(self):
        for reader in sorted(self.readers, key=lambda x: x.name):
            reader.display_info()

    def print_list_by_borrow_date_or_fine(self):
        sort_key = input('Sort by "borrow_date" or "fine"? ')
        if sort_key.lower() in ["borrow_date", "fine"]:
            for reader in sorted(self.readers, key=lambda x: getattr(x, sort_key.lower()), reverse=True):
                reader.display_info()
        else: 
            print('Sort key must be "borrow_date" or "fine".')

    def show_list_of_readers_with_filter(self):
        category = input("Enter category you want to filter: name | book_title | status | fine \n")
        value = input("Enter value want to filter out: ")
        if category.lower() in ['name', 'book_title', 'status', 'fine']:
            for reader in self.readers:
                if getattr(reader, category.lower()) == value.title():
                    reader.display_info()
                elif getattr(reader, category.lower()) == int(value):
                    reader.display_info()
        else:
            print("Invalid category. Please try again!")

    def add_returned_book(self):
        returned = False
        name = input("Enter name of the reader returning the book: ")
        if self.check_reader(name):
            book = input("Enter name of the book: ")
            for reader in self.readers:
                if reader.name == name.title() and reader.book_title == book.title():
                    reader.status = 'True'
                    returned = True
                    print("Book return status updated successfully.")
            return returned
        else:
            print("Reader not found.")

    def add_fine_to_reader(self, name):
        for reader in self.readers:
            reader.fine += 100
            print("Fine added successfully.")

    def save_to_file(self):
        file = open('reader.txt', 'w')
        for reader in self.readers:
            file.write(f"|{reader.name}|{reader.email}|{reader.phone_number}|{reader.book_title}|{reader.borrow_date}"
                       f"|{reader.return_date}|{reader.status}|{reader.fine}\n")
        file.close()
        print("Data saved to file successfully.")

    def check_reader(self, name):
        for reader in self.readers:
            if reader.name == name.title():
                return True
            else:
                return False

    def check_return_dates(self):
        count = 0
        for reader in self.readers:
            if reader.to_dict()['return_date'] < datetime.now().strftime('%Y-%m-%d'):
                count += 1
                self.add_fine_to_reader(reader.name)  # Fine amount
                print(f"Fine issued to {reader.name} for late return of book: {reader.book_title}")
        if count == 0:
            print("No reader is gave fine issued.")
