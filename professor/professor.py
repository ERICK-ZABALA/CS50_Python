import random

def main():
    level = get_level()
    value = generate_intiger(level)
    game(value)

def get_level():

    while(True):
        try:
            level = int(input("Level:").strip())
            if (level == 1) or (level == 2) or (level == 3):
                # print(level)
                return level

        except ValueError:
            pass
        else:
            pass

def generate_intiger(level):
    # print("Level: ",level)
    if level == 1:
        value_start = 0
        value_final = 9
    elif level == 2:
        value_start = 10
        value_final = 99
    else:
        value_start = 100
        value_final = 999
    return value_start, value_final

def game(value):
    counter = 0
    counter_good = 0
    while(True):
        try:

            x = random.randrange(value[0],value[1])
            y = random.randrange(value[0],value[1])

            if ((counter_good + counter) == 10):
                print("Score:",counter_good)
                return 0

            while(True):
                sum = x + y
                print(f"{x} + {y} = ",end="")
                #print( x, " + ", y ," = ", end= "")
                result = int(input().strip())

                if (sum == result):
                    # print (result)
                    counter_good = counter_good + 1
                    break
                else:
                    print("EEE")
                    counter = counter + 1

                if counter == 3:
                    print(f"{x} + {y} = {sum}")
                    # print( x, "+", y,"=", sum)
                    print("Score: 9")
                    return 0

        except ValueError:
            pass
        else:
            pass

if __name__ == "__main__":
    main()