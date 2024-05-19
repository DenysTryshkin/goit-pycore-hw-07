from phone import Phone
from name import Name
from birthday import Birthday

class Record:


    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def __str__(self):
        contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"
        return contact_info
    

    def add_phone(self, number):
        self.phones.append(Phone(number))


    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)


    def edit_phone(self, previous_number, new_number):
        for phone in self.phones:
            if phone.value == previous_number:
                phone.value = new_number


    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
            
    def add_birthday(self, date):
        self.birthday = Birthday(date)

