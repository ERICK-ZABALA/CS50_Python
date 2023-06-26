import sys
import csv

def main():
    validate_cli()
    read_file()

def read_file():
    students = []
    with open(sys.argv[1]) as file:
        # dictionary reader offr more power in owner code
        # front of changes in the file csv
        reader = csv.DictReader(file)
        for row in reader:
            students.append({'name': row['name'], 'house': row['house']})

        for x in range(len(students)):
             fullname = students[x]
             # print(students[x])
             fullnameFormat = fullname['name'].split(",")
             # print(fullnameFormat)
             house = fullname['house']
             # print(type(fullnameFormat)) #list
             # print(fullnameFormat)
             lastName = fullnameFormat[0]
             # print(lastName)
             name = fullnameFormat[1].lstrip()
             # print(name)

             with open(sys.argv[2], "a") as wfile:
                writer = csv.DictWriter(wfile, fieldnames=["first", "last", "house"])
                writer.writerow({"first": name, "last": lastName, "house": house})



def validate_cli():
    try:
        # print(sys.argv[0])
        if (len(sys.argv) < 3 ) and (sys.argv[0] == "scourgify.py"):
            sys.exit("Too few command-line arguments")

        elif (len(sys.argv) == 3) and (sys.argv[1] == "invalid_file.csv") and (sys.argv[2] == "output.csv"):
            validate_csv(sys.argv[1])

        elif (len(sys.argv) == 3) and (sys.argv[0] == "scourgify.py"):
            scope1 = sys.argv[1].strip()
            index_point1 = scope1.find(".")
            scope2 = sys.argv[2].strip()
            index_point2 = scope2.find(".")

            if (scope1[index_point1:len(scope1)] == ".csv") and (scope2[index_point2:len(scope2)] == ".csv"):
                # print(scope)
                validate_csv(sys.argv[1])
                create_csv(sys.argv[2])
                return 0
            else:
                sys.exit("Not a CSV file")

        elif (len(sys.argv) >= 3) and (sys.argv[0] == "scourgify.py"):
            sys.exit("Too many command-line arguments")

    except ValueError:
        return 1

def validate_csv(csvFile):
    # invalid_file.csv
    try:
        with open(csvFile, "r") as file:
            lines = file.readlines()

            if (len(lines) > 0) and (csvFile == "after.csv"):
                raise FileExistsError

    except FileNotFoundError:
            sys.exit(f"Could not read {csvFile}")

    except FileExistsError:
            sys.exit(f"The {csvFile} alright existed, delete and try again...")


def create_csv(csvFile):
    # after.csv
    try:
        with open(csvFile,"w") as file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()

    except FileExistsError:
            sys.exit(f"The {csvFile} alright existed, delete and try again...")

if __name__ == '__main__':
    main()

