import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # 275.3.6.28
    try:

        if (re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip)):


            numbers = ip.strip().split(".")
            numbers = [int(i) for i in numbers]
            #print(numbers)
            #print(type(numbers))
            for x in numbers:
                if str(x).isdigit():
                    print()
                else:
                    return False


            counter = 0
            for x in numbers:
                if (x > -1) and (x < 256):
                    counter = counter + 1
            #print(counter)
            if counter == 4:
                return True
            else:
                return False
        else:
            return False

    except ValueError:
        sys.exit(1)






if __name__ == "__main__":
    main()