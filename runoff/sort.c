#include <cs50.h>
#include <stdio.h>
#include <string.h>

int sort [] = {};

int selection_sort (int i, int look, int n, int size, int scope[]);

int main (void)
{
    // i to n 0 to xxx number to look
    // order 0 to 100
    int i = 0;
    int look = 0;
	int n = 50;
    int size = 8; // size array

    int scope [8]={10,20,15,15,20,30,40,45};
    int minimo = selection_sort(i, look, n, size, scope);
    printf("valor minimo: %i\n",minimo);

    return 0;
}

int selection_sort (int i, int look, int n, int size, int scope[])
{
    //int i,look = 0;
	//int n = 8;
    // scope [n] from 0 to n
    // read each position of array 0-7
    // int scope [8]={5,2,7,4,1,6,3,0}
    // int scope [5]={2,0,3,5,2};
    int counter = 0;
    for (int j=0; j < n; j++)
    {

        for (i = counter; i < size; i++)
        {
            if (scope[i] == look)
            {
                //swap
                sort[counter]= scope[counter];//5
                scope[counter] = scope[i]; // save 0 in array scope [0]
                scope[i] = sort[counter];
                counter = counter + 1;
            }
        }

        look = look + 1;


        //selection_sort (look, look, n, size);

	}
    return scope[0];
}