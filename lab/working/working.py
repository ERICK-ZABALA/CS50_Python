import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):

    try:
        # format1 = '^([1-9][0-9]*):*([0-5][0-9]) ([A_P][M]) to ([1-9]:[0-5][0-9] [A_P][M])$'
        # 9:00 AM to 5:00 PM
        if matches := re.search(r'^([1-9][0-9]*):*([0-5][0-9]) ([A_P][M]) to ([1-9]):([0-5][0-9]) ([A_P][M])$',s):
            # print (matches.groups())

            from_hours = int(matches.group(1))
            from_minutes = int(matches.group(2))
            to_hours = int(matches.group(4))
            to_minutes = int(matches.group(5))

            if (matches.group(3).strip().lower() != "am"):
                from_hours = from_hours + 12

            if (matches.group(6).strip().lower() != "am"):
                to_hours = to_hours + 12


            #print("format1")
            return f"{from_hours:02}:{from_minutes:02} to {to_hours:02}:{to_minutes:02}"

        # formato2 =
        # 9 AM to 5 PM
        # '^([1-9] *[0-9]*):*([0-5]*[0-9]* )([A_P][M] )to ([1-9]:* *[0-5]*[0-9]* *)([P_A][M])$'
        elif matches := re.search(r'^([1-9] *[0-9]*):*([0-5]*[0-5]* )([A_P][M] )to ([1-9]*[0-9]*):*( *[0-5]*[0-5]*) *([P_A][M])$',s):
            # print (matches.groups())
            from_hours = int(matches.group(1))
            from_minutes = 0
            to_hours = int(matches.group(4))
            to_minutes = 0
            if (matches.group(3).strip().lower() != "am"):
                from_hours = from_hours + 12
                if (from_hours == 24):
                    from_hours = 0
            elif (matches.group(3).strip().lower() == "am"):
                if (from_hours == 12):
                    from_hours = 0

            if (matches.group(6).strip().lower() != "am"):
                to_hours = to_hours + 12
                if (to_hours == 24):
                    to_hours = 12

            # print("format2")
            # print(valid_hour)
            return f"{from_hours:02}:{from_minutes:02} to {to_hours:02}:{to_minutes:02}"

    except ValueError:
        pass
    else:
        raise ValueError




if __name__ == "__main__":
    main()