def main():
    while(True):
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            return 0

        except TypeError:
            pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def convert(fraction):

    fraction = fraction.split("/")
    if not fraction[0].isnumeric():
        raise ValueError
    if not fraction[1].isnumeric():
        raise ValueError

    x = int(fraction[0])
    y = int(fraction[1])
    # print(data)
    # print(x)
    # print(y)
    if (y==0):
        raise ZeroDivisionError

    if (x > y):
        raise ValueError

    result = (round((x/y)*100))
    return result

def gauge(percentage):
          if percentage <= 1:
            return ("E")
          elif percentage >= 99:
            return ("F")
          else:
            percentage = str(percentage) + "%"
            return (percentage)


if __name__ == "__main__":
    main()
