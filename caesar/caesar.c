#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int count_letters(string plaintext);
int alpha_index (int letter);
int ciphertext_formula (int index, int key);
int ciphertext_translate (int ciphertext);

int C = 0;
int k = 0;

int main(int argc, string argv[])
{
     int a = 0;
     int b = 0;
     int counter_alpha = 0;
     int counter_digits = 0;

    if (argv[1] == 0)
     {
            printf ("Usage: ./caesar key\n");
            return 1;
     }

     string key1 = argv[1];
//     printf ("key1: %s\n",key1);
     for (int i =0; i<(strlen(argv[1])); i++)
        {
            a = isalnum (key1[i]);
            b = isdigit (key1[i]);
//            printf("alfhanum: %i\n",a);
//            printf("digit: %i\n",b);

            if (a!=0)
            {
              counter_alpha = counter_alpha + 1;
//              printf ("counter alpha: %i \n",counter_alpha);
            }
            if (b!=0)
            {
              counter_digits = counter_digits + 1;
//              printf ("counter digits: %i \n",counter_digits);
            }
        }

     if ((argc == 2) && (counter_digits == strlen(argv[1])))
        {
           // receive a correct digit
//           printf("Argv[1]: %s\n", argv[1]);
           // exist an argument
//           printf("word registered: %i\n",argc);

           //convert from string to initiger Argv[1]:xx
           k = atoi(argv[1]);
//           printf("Key: %i\n", k);

           //Request a plaintext to store as string in plaintext variable.
           string plaintext = get_string("plaintext: ");

           int numLetters = count_letters(plaintext);
//           printf("%i letters\n",numLetters);

           int numtext = strlen(plaintext);
//           printf("length: %i\n",numtext);

           int i=0;
           char result [strlen(plaintext)];


           for (i=0; i<(strlen(plaintext)); i++)
           {

                int position = alpha_index (plaintext[i]);
                int cipher = ciphertext_formula (position,k);
                result [i] = (char)ciphertext_translate (cipher);
//                printf("result char: %c\n",result[i]);

                if ((islower(plaintext[i])) && (islower((int)result[i]+32)))
                {
                    result[i] = tolower(result[i]);
//                    printf("result lower if: %c\n",result[i]);
                }
                else if ((isupper(plaintext[i])) && (isupper((int)result[i])))
                {
                    result[i] = toupper(result[i]);
//                    printf("result upper if: %c\n",result[i]);
                }

           }

            printf("ciphertext: %s\n",result);

        }
     else if ((argc == 3) && (counter_digits == strlen(argv[1])))
     {
        printf ("Usage: ./caesar key\n");
        return 1;
     }

     else if ((argc == 2) && (counter_alpha != strlen(argv[1])))
        {   //alphanumeric
            printf ("Usage: ./caesar key\n");
            return 1;
        }

    else if ((argc == 2) && (counter_digits != strlen(argv[1])))
        {   // if receive no digits
            printf ("Usage: ./caesar key\n");
            return 1;
        }
    else
    {
          // if receive no digits
            printf ("Usage: .../caesar key\n");
            return 1;

    }

       // printf("argv[1]: %s\n",argv[1]);k
       // int l = strlen(argv[1]);
       // printf("intiger length: %i\n",l);

}

// Count letters function
int count_letters(string plaintext)
{
    int i = 0;
    int count = 0;

    for (i = 0; i < (strlen(plaintext)); i++)
    {
        if (islower(plaintext[i]) || isupper(plaintext[i]))
        {
            count = count + 1;
            //printf("numero de letras: %i text: %c\n",count,text1[i]);
        }
    }
    return count;
}
// generate index for each letter
int alpha_index (int letter)
{
    if ((letter > 64) && (letter < 91))
    {
    //letter = 72;
    int index = letter - 65;
    return index;
    }
    else if ((letter > 96) && (letter < 123))
    {
//    printf ("letter num:%i\n",letter);
    int capital = letter - 32 - 65;
//    printf ("index:%i\n",capital);
    return capital; // 7
    }
    else if (letter == 32)
    {
    return 32;
    }
    else if (letter == 44)
    {
     return 44;
    }
    else
    {
        return 1;
    }
}

// formula cyphertext
int ciphertext_formula (int index, int key)
{
    if (index == 32)
    {
        //space char
        return 32;
    }
    else if (index == 44)
    {
        //space char
        return 44;
    }
    else
    {
    // formula ciphertext
    // Ci = (pi + k) % 26
    C = (index + key) % 26;
//    printf ("C= %i\n",C);
    return C;
    }
}
int ciphertext_translate (int ciphertext)
{
    if (ciphertext == 32)
    {
        return 32;
    }
    else if (ciphertext == 44 )
    {
        return 44;
    }
    else
    {
    // translate ciphertext to ASCII
    int translate = ciphertext + 65;
    return translate;
    }
}