#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int num = 0;

    do

    {

        int height = 0;
        int dot = 0;
        int hash = 0;
        int row = 0;

        // if value insert is between 0 to 9 run this follow lines:
        height = get_int("Height: ");

        if (height > 0  && height < 9)
        {
            //for row
            for (int k = 0; k < height; k++)
            {
                //for dot
                for (int i = 0; i < height - 1 - k; i++)
                {
                    printf(" ");
                }
                //for hash
                hash = hash + 1;

                for (int j = 0; j < hash; j++)
                {
                    printf("#");
                }

                row = k + 1;
                printf("\n");
            }

            break;
        }

    }

    while (num == 0);
    return 0;
}