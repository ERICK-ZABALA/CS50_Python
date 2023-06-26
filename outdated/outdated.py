

def main():
    while(True):
        try:
            #YYY-MM-DD
            date = input("Date: ").strip().lower()
            coma = str(date)

            date = date.replace(",","").replace("/"," ")
            #print(type(date))
            #print(date)

            date = date.split()
            # text or num
            # print(type(date))
            # print(date)

            # March 12, 1234
            month = get_month(date,coma)
            #print(month)

            if (month == 0):
                raise ValueError

            day = get_day(date)
            #print(day)
            if (day == 0):
                raise ValueError

            year = get_year(date)
            #print(year)

            print(f"{year:04}-{month:02}-{day:02}")


        except ValueError:
            # print("Value Error!!!")
            pass
        else:
            break

def get_day(day):
    if (int(day[1]) < 31):
        return int(day[1])
    else:
        print(f"error: ValueError: day:{day[1]} > 31")
        return 0

def get_month(date, coma=None):
    months = ["january", "february", "march", "april", "may", "june", "july", "august",
            "september", "october", "november", "december"]

    for month in range (12):
        if (date[0] == months[month]):
            if (coma.find(",") == -1):
                print(f"error: ValueError: coma no exist")
                return 0
            else:
                return month + 1

    #9/8/1636 <<< 1636-09-08
    if (str(date[0]).isdigit()) and (int(date[0])< 13):
        return int(date[0])
    else:
        print(f"error: ValueError: month:{date[0]} > 12")
        return 0

def get_year(year):
    if (year[2].isdigit) and (len(year[2]) == 4):
        return int(year[2])

main()