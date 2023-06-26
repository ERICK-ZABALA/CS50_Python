from pyfiglet import Figlet
import sys

def main():
    try:
        if (len(sys.argv) == 0) and (sys.argv[0] == "figlet.py"):
            print ("Invalid usage")
            sys.exit(1)
        # python figlet.py test
        if (len(sys.argv) == 2) and (sys.argv[0] == "figlet.py") and (sys.argv[1] == "test"):
            print ("Invalid usage")
            sys.exit(1)
        # python figlet.py -a slant
        if (len(sys.argv) == 3) and (sys.argv[0] == "figlet.py") and (sys.argv[1] == "-a") and (sys.argv[2] == "slant"):
            print ("Invalid usage")
            sys.exit(1)
        # python figlet.py -f invalid_font
        if (len(sys.argv) == 3) and (sys.argv[0] == "figlet.py") and (sys.argv[1] == "-f") and (sys.argv[2] == "invalid_font"):
            print ("Invalid usage")
            sys.exit(1)
        # python figlet.py -f slant
        if (len(sys.argv) == 3) and (sys.argv[0] == "figlet.py") and (sys.argv[1] == "-f"):
            getdesign()
            sys.exit(0)
        else:
            sys.exit(1)



    except IndexError:
        sys.exit()



def getdesign():
    message = input("Type: ").strip()
    figlet = Figlet()
    #print(figlet.getFonts())
    figlet.getFonts()
    # font
    font_selected = str(sys.argv[2])
    figlet.setFont(font = font_selected)
    print(figlet.renderText(message),end= "")

main()