import re



def main():
    print(count(input("Text: ")))


def count(s):
    capture = re.findall(r'\bum\b', s, re.IGNORECASE)
    num = len(capture)
    return num


if __name__ == "__main__":
    main()

