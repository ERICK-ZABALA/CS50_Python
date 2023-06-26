import sys
# python adieu.py
names = []
while (True):
    try:
        type = input().strip().title()
        names.append(type)


    except EOFError:
        print("Adieu, adieu, to", end=" ")
        num = len(names)

        if num == 1:
            print(names[num-1])
            sys.exit(0)
        if num == 2:
            print(names[0] + " and " + names[1])
            sys.exit(0)

        if num > 2:
            for i in range(num-1):
                print(names[i] + ", ", end="")

            print("and ", end="")
            print(names[num-1])
            sys.exit(0)




