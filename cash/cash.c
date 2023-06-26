#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("Coin: %i\n", coins);
    printf("Quarter (25$): %i\n", quarters);
    printf("Dimes (10$): %i\n", dimes);
    printf("Nickels (5$): %i\n", nickels);
    printf("Pennies (1$): %i\n", pennies);
}

int get_cents(void)
{
    // interface UI user to put the quantity of cents.
    int count = 0;
    float cents = 0;

    do
    {
        cents = get_int("Cents: ");

        if (cents < 0)
        {
            // go to the loop one more time
            count = 1;
        }
        else
        {
            // exit to loop and run all sequence of coding
            count = 2;
        }

    }

    while (count == 1);
    return (int) cents;
}

int calculate_quarters(int cents)
{
    // generate calculus 25 cents
    if (cents > 0 && cents < 25)
    {
        return 0;
    }
    else if (cents > 24 && cents < 50)
    {
        return 1;
    }
    else if (cents > 49 && cents < 75)
    {
        return 2;
    }
    else if (cents > 74 && cents < 101)
    {
        return 3;
    }
    else if (cents > 100 && cents < 124)
    {
        return 4;
    }
    else if (cents > 123 && cents < 151)
    {
        return 5;
    }
    else if (cents > 150 && cents < 176)
    {
        return 6;
    }

    else
    {
        return 0;
    }
}

int calculate_dimes(int cents)
{
    // generate calculus for 10 $ cents
    if (cents > 0 & cents < 8)
    {
        return 0;
    }
    else if (cents > 9 & cents < 20)
    {
        return 1;
    }
    else if (cents > 19 & cents < 30)
    {
        return 2;
    }
    else if (cents > 29 & cents < 40)
    {
        return 3;
    }
    else if (cents > 39 & cents < 50)
    {
        return 4;
    }
    else if (cents == 50)
    {
        return 5;
    }
    else
    {
        return 0;
    }
}

int calculate_nickels(int cents)
{
    // generate calculus for $5 cents

    if (cents > 0 & cents < 4)
    {
        return 0;
    }
    else if (cents == 5)
    {
        return 1;
    }
    else if (cents > 5 & cents < 10)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int calculate_pennies(int cents)
{
    // generate calculus for $1 cent.
    if (cents == 1)
    {
        return 1;
    }
    else if (cents < 5)
    {
        return cents;
    }
    else
    {
        return 0;
    }
}
