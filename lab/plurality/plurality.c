#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    int num = candidate_count;
    // number candidates is num
    for (int i = 0; i < num; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes = candidates[i].votes + 1;
            return true;
        }

    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    int tie1 = 0;
    int tie2 = 0;
    int winner = 0;
    string winner_name;
    string second_winner_name;
    string third_winner_name;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > winner)
        {
            winner_name = candidates[i].name;
            winner = candidates[i].votes;
        }
        else if (candidates[i].votes == winner && (tie1 == 0))
        {
            second_winner_name = candidates[i].name;
            tie1 = tie1 + 1;
            tie2 = tie1;
        }
        else if (candidates[i].votes == winner && (tie2 == 1))
        {
            third_winner_name = candidates[i].name;
            tie2 =  tie2 + 1;
        }
    }
    printf("%s\n", winner_name);

    if (tie1 == 1)
    {
        printf("%s\n", second_winner_name);

    }
    if (tie2 == 2)
    {
        printf("%s\n", third_winner_name);

    }


    return;
}