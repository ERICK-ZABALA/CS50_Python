#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    int numLetters = count_letters(text);
    int numWords = count_words(text);
    int numSentences = count_sentences(text);

    //printf("%i letters\n",numLetters);
    //printf("%i words\n",numWords);
    //printf("%i sentences\n",numSentences);

    // formula: index = 0.0588 * (L - 0.296) * (S - 15.8)

   
    // important maintain the same variable data in operation.

    L = ((float)numLetters / (float)numWords) * 100;
    S = ((float)numSentences / (float)numWords) * 100;

    //printf(" L:%f\n",L);
    //printf(" S:%f\n",S);

    index = round((0.0588 * L) - (0.296 * S) - 15.8);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", (int) index);
    }
}
// Count letters function
int count_letters(string text)
{
    int i = 0;
    int count = 0;

    for (i = 0; i < (strlen(text)); i++)
    {
        if (islower(text[i]) || isupper(text[i]))
        {
            count = count + 1;
            //printf("numero de letras: %i text: %c\n",count,text1[i]);
        }
    }
    return count;
}

// Count Words function
int count_words(string text)
{
    int i = 0;
    int count = 0;

    for (i = 0; i < (strlen(text) + 1); i++)
    {

        if (isspace(text[i]) || (text[i] == '\0'))
        {
            count = count + 1;
            //printf("numero de letras: %i text: %c\n",count,text1[i]);
        }
    }

    //printf("upos: %i\n", text[strlen(text)+1]);
    return count;
}

// Count Sentences function
int count_sentences(string text)
{
    int i = 0;
    int count = 0;

    for (i = 0; i < (strlen(text)); i++)
    {
        if ((text[i] == '.') || (text[i] == '!') || (text[i] == '?'))
        {
            count = count + 1;
            //printf("numero de letras: %i text: %c\n",count,text1[i]);
        }

    }

    //printf("upos: %i\n", text[strlen(text)+1]);
    return count;

}