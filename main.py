from address_book import AddressBook
from record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact does not exist!"
        except ValueError:
            return "Something went wrong"
        except IndexError:
            return "Please provide the required argument for the command."
    
    return inner

@input_error
def add_contact(args, book: AddressBook):
    if len(args) !=2:
        raise ValueError
    name, phone = args
    book.add_record(Record(name=name))
    return "Contact added."


@input_error
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        return "Invalid number of arguments. "
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        return ValueError
    else:
        record.edit_phone(old_number, new_number)
        return "Contact updated"

    

@input_error
def show_phone(args, book: AddressBook):
    if len(args) !=1:
        raise ValueError
    name = args[0]
    if name not in book:
        raise KeyError
    return book[name]
    

@input_error
def show_all(book: AddressBook):
    if not book:
        return "No contacts saved!"
    
    return "\n".join([f"{name}: {phone}" for name, phone in book.items()])


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        return "Invalid number of arguments."
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    else:
        return f"Contact '{name}' is not in the addressbook"


@input_error
def show_birthday(args, book):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name not in book:
        raise KeyError
    return book[name]["birthday"]


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

