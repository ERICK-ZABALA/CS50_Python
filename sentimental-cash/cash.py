#!/usr/local/bin/python
# shibang
# Cash in Python
from cs50 import get_float


def main():
    # Ask how many cents the customer is owed
    cents = get_cents()
    # Calculate the number of quarter to give the customer
    quarters = calculate_quarters(cents)
    cents = int(cents) - (int(quarters) * 25)

    # Calculate the number of dimmes t give the customer
    dimes = calculate_dimes(cents)
    cents = int(cents) - (int(dimes) * 10)

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = int(cents) - (int(nickels) * 5)

    pennies = calculate_pennies(cents)
    cents = int(cents) - (int(pennies) * 1)

    # Sum coins
    coins = int(quarters) + int(dimes) + int(nickels) + int(pennies)

    # Print total number of coins to give the customer
    print("Coin: ", coins)
    print("Quarter (25$): ", quarters)
    print("Dimes (10$): ", dimes)
    print("Nickels (5$): ", nickels)
    print("Pennies (1$): ", pennies)


def get_cents():
    count = 0
    cents = 0.0

    cents = get_float("Cents: ")
    print(cents)

    if cents > 0:
        cents = cents * 100
        count = 2
        return cents

    else:

        main()


def calculate_quarters(cents):

    if (cents / 25) > 0:
        return (int(cents/25))
    else:
        return 0


def calculate_dimes(cents):
    # Generate calculus for 10 $ cents
    if (cents / 10) > 0:
        return (int(cents/10))
    else:
        return 0


def calculate_nickels(cents):

    if (cents / 5) > 0:
        return (int(cents/5))
    else:
        return 0


def calculate_pennies(cents):
    # Generate calculus for $1 cent.
    if (cents / 1) > 0:
        return (int(cents/1))
    else:
        return 0


if __name__ == "__main__":
    main()
