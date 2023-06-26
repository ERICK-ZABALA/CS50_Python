#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
int selection_sort(int i, int look, int n, int size, int count_candidate[]);

bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            // candidates[i].votes = candidates[i].votes + 1;
            // preferences[voter][rank] = i;
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{

    // TODO
    //update vote counts for all no eliminated candidates
    int counter = 0;
    int vote = 0;
    int less_candidate_count = candidate_count;
    // count votes
    for (int j = 0; j < voter_count; j++)
    {
        vote = preferences[j][0]; // store value vote:candidate matrix preferences [0 0]
        if (candidates[vote].eliminated == true)
        {
            while (candidates[vote].eliminated == true)
            {
                counter = counter + 1;
                less_candidate_count = candidate_count - 1;
                vote = preferences[j][counter];
                if (less_candidate_count == 0)
                {
                    return;
                }
            }
            candidates[vote].votes = candidates[vote].votes + 1;
        }

        else if (candidates[vote].eliminated == false)
        {
            candidates[vote].votes = candidates[vote].votes + 1;
        }
    }
    // call each voter higher pref candidates who ha not yet been eliminated
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{

    int sum = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        sum = candidates[i].votes + sum;
    }

    // printf ("votes sum: %i\n",sum);
    // printf ("votes mitad: %i\n",sum/2);

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > (sum / 2))
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }

    return false;
}


int selection_sort(int i, int look, int n, int size, int count_candidate[])
{
    
    int sort [] = {};
    int counter = 0;
    for (int j = 0; j < n; j++)
    {

        for (i = counter; i < size; i++)
        {
            if (count_candidate[i] == look)
            {
                // swap
                sort[counter] = count_candidate[counter];
                // 5
                count_candidate[counter] = count_candidate[i];
                // save 0 in array scope [0]
                count_candidate[i] = sort[counter];
                counter = counter + 1;
            }
        }
        look = look + 1;
    }
    return count_candidate[0];
}
// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    int count = 0;
    int candidate_less = 0;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false)
        {
            count = count + 1;
        }
    }
    // all candidates still in the election state: false
    if (count == candidate_count)
    {

        // candidate less votes return
        for (int i = 0; i < candidate_count; i ++)
        {
            // candidates[i].name
            if (candidate_less < candidates[i].votes)
            {
                candidate_less = candidates[i].votes;

            }

        }
        // printf("candidate less votes: %i\n",candidate_less);

        return candidate_less;
    }

    // in this case exist a candidate true, need to ignore this candidate and
    // select de less (false candidate)

    if (count != candidate_count)
    {

        // candidate less votes return
        for (int i = 0; i < candidate_count; i ++)
        {
            //candidates[i].name
            if ((candidate_less < candidates[i].votes) && (candidates[i].eliminated == false))
            {
                candidate_less = candidates[i].votes;

            }
        }

    }
    return candidate_less;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
    int min_votes_candidates [] = {};
    bool min_eliminated_candidates [] = {};

    int counter = 0;
    int counter_false = 0;

    for (int i = 0; i < candidate_count; i++)
    {
        if ((min == candidates[i].votes) && (candidates[i].eliminated == false))
        {
            counter = counter + 1;
        }
        else if ((min != candidates[i].votes) && (candidates[i].eliminated == false))
        {
            return false;
        }
    }

    if (counter <= candidate_count)
    {
        // printf("tie!!! %i\n",counter);
        return true;
    }
    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    printf("candidate eliminated: %i\n", min);
    int counter = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (min == candidates[i].votes)
        {

            candidates[i].eliminated = true;
            printf("candidate name: %s\n", candidates[i].name);
            printf("candidate state: %d\n", candidates[i].eliminated);
            counter = counter + 1;
        }

    }

    return;
}