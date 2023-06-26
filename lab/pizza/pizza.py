import sys
import csv
from tabulate import tabulate

def main():

    while(True):
        validate_cli()
        break

    try:
        menu = []
        headers = []
        table = []

        with open(sys.argv[1],"r") as regular_file:
            reader= csv.reader(regular_file)
            for row in reader:
                menu.append(row)
            #print("Menu: ",menu)
            headers = menu[0].copy()
            #print("Headers: ",headers)
            table = menu[1:].copy()
            #print("Table: ",table)

            print(tabulate(table, headers, tablefmt="grid"))
            return 0



    except FileNotFoundError:
        sys.exit("File does not exist")


def validate_cli():
    try:
        # print(sys.argv[0])
        if (len(sys.argv) == 1) and (sys.argv[0] == "pizza.py"):
            sys.exit("Too few command-line arguments")

        elif (len(sys.argv) == 2) and (sys.argv[1] == "invalid_file.csv"):
            sys.exit("File does not exist")

        elif (len(sys.argv) == 2) and (sys.argv[0] == "pizza.py"):
            scope = sys.argv[1].strip()
            index_point = scope.find(".")
            if (scope[index_point:len(scope)] == ".csv"):
                # print(scope)
                return 0
            else:
                sys.exit("Not a CSV file")

        elif (len(sys.argv) >= 3) and (sys.argv[0] == "pizza.py"):
            sys.exit("Too many command-line arguments")

    except ValueError:
        return 1



if __name__ == '__main__':
    main()

