#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
char LETTERS[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int compute_score(string word);
string capital_letter(string letter);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if ((score1) < (score2))
    {
        printf("Player 2 wins!\n");
        // printf("score2: %i\n",score2);
    }
    else if ((score1) > (score2))
    {
        printf("Player 1 wins!\n");
        // printf("score1: %i\n",score1);
    }
    else
    {
        printf("Tie!\n");
        // printf("score1: %i\n",score1);
        // printf("score2: %i\n",score2);
    }

}


int compute_score(string word)
{
    // TODO: Compute and return score for string
    word = capital_letter(word);
    // Compare table letter with capital_letters data
    int count = 0;
    int result[count];
    int add = 0;

    for (int i = 0; i < (strlen(word)); i++) //C ISCO
    {
        for (int j = 0; j < 26; j++)
        {

            if (word[i] == LETTERS[j])
            {
                printf("result puntos: %i\n", POINTS[j]);
                printf("result match letters: %c\n", LETTERS[j]);
                count = count + 1;

                add = POINTS[j] + add;
                printf("counter: %i\n", count);
            }
        }
    }

    return add;
}

string capital_letter(string letter)
{
    for (int i = 0; i < (strlen(letter)); i++)
    {
        letter[i] = toupper(letter[i]);

    }
    printf("capital letter word: %s\n", letter);
    return letter;

    /*Output: scrabble/ $ ./scrabble
            Player 1: C1sc0!,.
            Player 2: CiscO!234
            capital letter word: C1SC0!,.
            capital letter word: CISCO!234 */
}