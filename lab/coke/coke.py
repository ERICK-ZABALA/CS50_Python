bottle_coke = 50
coin = 0

Owed = 1
while (Owed > 0):
    print("Amount Due: ", end="")
    print(bottle_coke)
    print("Insert Coin: ", end="")
    coin = int(input().strip())
    match coin:
        case 50 | 25 | 10 | 5:
            bottle_coke = bottle_coke - coin
            if (bottle_coke == 0):
                print("Change Owed: ", bottle_coke)
                Owed = 0
            elif(bottle_coke < 0):
                bottle_coke = bottle_coke * (-1)
                print("Amount Owed: ", end="")
                print(bottle_coke)
                Owed = 0


