from datetime import datetime, timedelta
from collections import UserDict

class AddressBook(UserDict):


    def add_record(self, record):
        if self.data.get(record.name.value):
           raise KeyError(f"This name '{record.name.value}' is already taken by another user. Please choose another name.")
        self.data[record.name.value] = record


    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f"No record found with the name '{name}'.")
            return None


    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Record with the name '{name}' successfully deleted.")
        else:
            print(f"No record found with the name '{name}'. Deletion not performed.")


    def get_upcoming_birthdays(self):
        today = datetime.today().date()

        greetings = []

        for name, record in self.data.items():
            birthday = record.birthday  # Отримання дня народження з об'єкта запису
            birthday_this_year = birthday.replace(year=today.year)
    
            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            days_until_birthday = (birthday_this_year - today).days

            while birthday_this_year.weekday() <= 5:
                birthday_this_year += timedelta(days=1)
            
            if 0 <= days_until_birthday <= 7:
                greetings.append({"name": record.name.value, "greeting_date": birthday_this_year})
    
        return greetings
