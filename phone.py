from field import Field

class Phone(Field):

    def __init__(self, number):
        self.value = self.correct_number(number)

    def correct_number(self, number):
        if len(number) == 10 and number.isdigit():
            return number
        else:
            raise ValueError("Phone number must include exactly 10 digits") 


        