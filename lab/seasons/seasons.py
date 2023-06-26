from datetime import date
import sys
import inflect

class DateBithday:
    def __init__(self, birthday_date, year=0, month=0, day=0, minutes=None, words=None):
        self.birthday_date = birthday_date # assigned the actual data when init
        self.NUM_MINUTES = 60

        self.year = year
        self.month = month
        self.day = day
        self.minutes = minutes
        self.words = words

    def __str__(self):
        #return f"{self.words.capitalize()} minutes"
        # I put self.birthday_date because that is defined.
        # f"Birthday Date: {self.birthday_date} Minutes: {self.minutes} Words: {self.words}"

        return f"{self.words.capitalize()} minutes"

        #print(today) #2022-11-12
        #today = date.today()
        #print(f"Today: {today.year}-{today.month}-{today.day}")

    def get_difference(self):

        if self.year == 0 and self.month == 0 and self.day == 0:
            today = date.today()
        else:
            today = date(self.year, self.month, self.day)

        #print(type(today))
        difference = date.__sub__(today, self.birthday_date)
        #print(difference)
        self.minutes = difference.total_seconds()/self.NUM_MINUTES

    def convert_numbers_words(self):
        convert = inflect.engine()
        self.words = convert.number_to_words(int(self.minutes), andword="")





################################################################################

def main():
    try:

        type = input("Date of Birth: ").strip()
        dateBirth = get_birthday(type)
        dateBirth.get_difference()
        dateBirth.convert_numbers_words()
        print(dateBirth)

    except ValueError:
        print ("Invalid date")
        sys.exit(1)

def get_birthday(type):
    birthday_date = date.fromisoformat(type)
    # return the variable type and birthday_date to class DateBithday
    return DateBithday(birthday_date)


if __name__ == "__main__":
    main()
