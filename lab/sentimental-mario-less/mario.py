# TODO
import cs50
from cs50 import get_int

while True:

    hash = 0
    try:
        height = get_int("Height: ")
    except ValueError:
        print("That is not a value 1 to 8")
        exit()

    if height > 0 and height < 9:
        # row
        for i in range(height):
            # for dot
            for j in range(height-1 - i):
                print(" ", end="")

            # for hash
            hash = hash + 1
            for k in range(hash):
                print("#", end="")
            row = i + 1
            print()

        break