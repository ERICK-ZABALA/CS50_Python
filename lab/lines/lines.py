import sys

def main():

    while(True):
        validate_cli()
        break
    lines = []
    try:
        f = open(sys.argv[1],"r")
        lines= f.readlines()
        # print(lines)
        # print(type(lines))

        number_lines = len(lines)
        # print("Lineas: ",number_lines)
        counter_comment = 0
        counter_white_comment = 0

        for line in range(len(lines)):
            texto = str(lines[line])
           # print(texto)
           # print(type(texto))
            if texto.strip().startswith("#"):
                counter_comment = counter_comment + 1
            if texto.isspace():
                counter_white_comment = counter_white_comment + 1
        # print("comment number: ",counter_comment)
        # print("comment blank number: ",counter_white_comment)
        result = number_lines - counter_comment - counter_white_comment
        print(f"count lines: {result}")



    except FileNotFoundError:
        sys.exit()


def validate_cli():
    try:
        # print(sys.argv[0])
        if (len(sys.argv) == 1) and (sys.argv[0] == "lines.py"):
            sys.exit("Too few command-line arguments")
        elif (len(sys.argv) == 2) and (sys.argv[0] == "lines.py"):
            scope = sys.argv[1].strip()
            index_point = scope.find(".")
            if (scope[index_point:len(scope)] == ".py"):
                # print(scope)
                return 0
            else:
                sys.exit("Not a Python file")
        elif (len(sys.argv) == 2) and (sys.argv[0] == "lines.py") and (sys.argv[1] == "non_existent_file.py"):
                sys.exit("File does not exist")
        elif (len(sys.argv) >= 3) and (sys.argv[0] == "lines.py"):
                sys.exit("Too many command-line arguments")

    except ValueError:
        return 1



if __name__ == '__main__':
    main()

