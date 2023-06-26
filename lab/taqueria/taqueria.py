

def main():
    total = 0
    while (True):
        try:
            item = input("Item: ").strip().title()
            if item == "":
                return 1
                # print(item)
            total = menu (item) + total
            print("Total: ${:.2f}".format(total))

        except EOFError:
            print()
            return 1
        except KeyError:
            pass

def menu(item):

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    return menu[item]

main()