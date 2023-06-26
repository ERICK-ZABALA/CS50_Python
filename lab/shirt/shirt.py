

import sys
import os
from PIL import Image, ImageOps

def main():
    try:
        validate_command_line()

        shirt = Image.open("shirt.png")
        size = shirt.size
        # before1.jpg
        image_sesamo = Image.open(sys.argv[1], mode='r')
        image_sesamo_sized = ImageOps.fit(image_sesamo, size)
        image_sesamo_sized.paste(shirt, shirt)
        image_sesamo_sized.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def validate_command_line():
    try:
        if (sys.argv[0] == "shirt.py"):
            if len(sys.argv) < 3:
                sys.exit("Too few command-line arguments")
            elif len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")
            if len(sys.argv) == 3:
                #print(os.path.splitext(sys.argv[1]))
                #print(os.path.splitext(sys.argv[2]))
                ext1 = os.path.splitext(sys.argv[1])
                ext2 = os.path.splitext(sys.argv[2])
                #print(ext1[1])
                #print(ext2[1])
                #python shirt.py before1.jpg after1.png
                if ext1[1] != ext2[1] and ext2[1] != ".jpeg" and ext2[1] != ".png" and ext2[1] != ".jpg":
                    sys.exit("Invalid output")
                elif ext1[1] != ext2[1] and (ext2[1] == ".jpeg" or ext2[1] == ".png" or ext2[1] ==".jpg"):
                    sys.exit("Input and output have different extensions")
                elif ext1[1] == ext2[1] and (ext2[1] == ".jpeg" or ext2[1] == ".png" or ext2[1] == ".jpg") and os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
                    print(f"File correct: {sys.argv[1].rstrip()} {sys.argv[2].rstrip()}")
                    return 0
                elif ext1[1] == ext2[1] and (ext2[1] == ".jpeg" or ext2[1] == ".png" or ext2[1] == ".jpg") and (False == os.path.isfile(sys.argv[1])) and (False == os.path.isfile(sys.argv[2])):
                    sys.exit("Input does not exist")
            else:
                sys.exit("File no commpling with specifications")
    except FileNotFoundError:
        sys.exit()

if __name__ == "__main__":
    main()