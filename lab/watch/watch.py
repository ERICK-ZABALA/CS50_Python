import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #https://www.youtube.com/embed/xvFZjo5PgG0


    if matches := re.search(r'(<iframe src=")(http)(s)*:\/\/(www.)*(youtube.com\/embed\/)([a-z_A-Z_0-9]+)("><\/iframe>)*',s):
        return f"https://youtu.be/{matches.group(6)}"





if __name__ == "__main__":
    main()