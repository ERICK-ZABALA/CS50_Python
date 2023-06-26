import random
import sys

def main():

    while (True):
        try:
            type = int(input("Level: ").strip())

            if type < 0:
                raise EOFError
            elif type > 0:
               number = random.randint(1,type)
               guess = int(input("Guess: ").strip())

               if number < 0:
                raise EOFError
               elif guess < number:
                print("Too small!")

               elif guess > number:
                print("Too large!")
                
               elif guess == number:
                print("Just right!")
                sys.exit(0)

        except EOFError:
            pass

        except ValueError:
            pass


main()