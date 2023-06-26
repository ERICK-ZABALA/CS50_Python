
//Header Files
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

/* only used in string related operations */
typedef struct String string;
struct String
{
    char *str;
};

char *input(FILE *fp, int size, int has_space)
{
    int actual_size = 0;
    char *str = (char *)malloc(sizeof(char)*(size+actual_size));
    char ch;
    if(has_space == 1)
    {
        while(EOF != (ch=fgetc(fp)) && ch != '\n')
        {
            str[actual_size] = ch;
            actual_size++;
            if(actual_size >= size)
            {
                str = realloc(str,sizeof(char)*actual_size);
            }
        }
    }
    else
    {
        while(EOF != (ch=fgetc(fp)) && ch != '\n' && ch != ' ')
        {
            str[actual_size] = ch;
            actual_size++;
            if(actual_size >= size)
            {
                str = realloc(str,sizeof(char)*actual_size);
            }
        }
    }
    actual_size++;
    str = realloc(str,sizeof(char)*actual_size);
    str[actual_size-1] = '\0';
    return str;
}
/* only used in string related operations */


/*
 * inputNum, represents the number of rows and columns of the chess board (N).
 */
void  funcChessBoard(int inputNum)
{
    // Write your code
   int counter = 0;
   int times = 0;
   int i, j = 0;


   while (inputNum > counter)
   {

    if (times == inputNum)
            {
            i = 1;
            j = 1;
            counter = inputNum + 1;
            }

    if (counter == 0)
    {
        // times = times + 1;
        if (times == inputNum)
        {
            i = 1;
            j = 1;
            counter = inputNum + 1;
        }
    }
    for ( i = 0; i < 1; i++)
    {
       printf( "W ");
       counter = counter + 1;

       if (counter == inputNum)
        {
        printf("\n");
        counter = 0;
        times = times + 1;
          if (times == inputNum)
            {
            i = 1;
            j = 1;
            counter = inputNum + 1;
            }
        }

    }

    if (times == inputNum)
            {
            i = 1;
            j = 1;
            counter = inputNum + 1;
            break;
            }

    for (j = 0; j < 1; j++)
    {
       printf( "B ");
       counter = counter + 1;
       if (counter == inputNum)
        {
        printf("\n");
        counter = 0;
        times = times + 1;
          if (times == inputNum)
            {
            i = 1;
            j = 1;
            counter = inputNum + 1;
            }

        }


    }
   }


}

int main()
{
    int inputNum;
	printf("Input: ");
    //input for inputNum
	scanf("%d", &inputNum);
    printf("\n");
    if (inputNum > 999)
    {
        return 1;
    }


	funcChessBoard(inputNum);
    return 0;
}