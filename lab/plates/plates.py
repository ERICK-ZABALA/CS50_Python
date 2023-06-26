

def main():
    plate = str(input("Plate: ").strip())
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    match s:
        case "CS05" | "CS50P2":
            return False

    if (s[0:2] != s[0:1].isdigit()):
        # print(s[0:2])
        if (len(s) <= 6):
            if (s[len(s)-1].isdigit()):
                if(s[len(s)-3] != '0'):
                    return True
            elif s.isalpha():
                if len(s) > 1:
                    return True


if __name__ == "__main__":
    main()
