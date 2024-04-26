from datetime import datetime, timedelta
import copy

class Reader:
    def __init__(self, name, email, phone_number, title_of_book, borrow_date):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.title_of_book = title_of_book
        self.borrow_date = datetime.strptime(borrow_date, '%Y-%m-%d')
        self.return_date = self.borrow_date + timedelta(days=30)
        self.status = False
        self.fine = 0

    def display_info(self):
        print(f"| {self.name} | {self.email} | {self.phone_number} | {self.title_of_book} | {self.borrow_date} | "
              f"{self.return_date} | {self.status} | {self.fine} |")

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
                if reader.name == name.title() and reader.title_of_book == book.title():
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

    def show_list_of_readers_with_filter(self, **filters):  # Cần cải thiện UX, filter name/ book tittle/ status
        filtered_readers = copy.deepcopy(self.readers)
        for key, value in filters.items():
            filtered_readers = [reader for reader in filtered_readers if getattr(reader, key) == value]
        for reader in filtered_readers:
            reader.display_info()

    def add_returned_book(self):
        returned = False
        name = input("Enter name of the reader returning the book: ")
        if self.check_reader(name):
            book = input("Enter name of the book: ")
            for reader in self.readers:
                if reader.name == name.title() and reader.title_of_book == book.title():
                    reader.status = True
                    returned = True
                    print("Book return status updated successfully.")
            return returned
        else:
            print("Reader not found.")

    def add_fine_to_reader(self, name, fine):
        reader = self.check_reader(name)
        if reader:
            reader.fine += fine
            print("Fine added successfully.")

    def save_to_file(self):
        file = open('reader.txt', 'w')
        for reader in self.readers:
            file.write(f"|{reader.name}|{reader.email}|{reader.phone_number}|{reader.title_of_book}|{reader.borrow_date}"
                       f"|{reader.return_date}|{reader.status}|{reader.fine}\n")
        file.close()
        print("Data saved to file successfully.")

    def check_reader(self, name):
        for reader in self.readers:
            if reader.name == name.title():
                return True
            else:
                return False
