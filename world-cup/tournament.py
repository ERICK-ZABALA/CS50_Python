#!/usr/local/bin/python

# Simulate a sports tournament
import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    ratings = []
    # TODO: Read teams into memory from file
    filename = sys.argv[1]
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            team_list = row["team"]
            rating_list = int(row["rating"])

            row["rating"] = int(row["rating"])
            teams.append(row)
            # rating = int(rating)
            # output:<class 'str'>
            # teams.append(team_list)
            ratings.append(rating_list)
        # print(teams)
        # print(ratings)
    # +print(type(teams))

    # teams = {teams[i]: ratings[i] for i in range(len(teams))}

    # +print(type(teams))
    # +print(teams)

    # print (len(teams))

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    for i in range(N):
        winner = simulate_tournament(teams)
       # winner = list(winner.keys())
       # winner = str(winner[0])
      # print("win:",winner)
        if winner in counts:
            counts[winner] += 1

        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""

    winners = []
    winners_team = []
    winners_rating = []
    # +print (teams)

    # dictKey = list(teams.keys())
    # print ("Key:",dictKey)
    # dictVal = list(teams.values())
    # print ("Values:",dictVal)
    # print (teams[0])
    # print (teams)
    # teams = teams.items()
    # print (teams)
    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):

        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
            # winners_rating.append(dictVal[i])
            # dict_winners = {winners_team[i]: winners_rating[i] for i in range(len(winners_team))}
            # dict_winners = winners.items()
            # print(dict_winners)
        else:
            winners.append(teams[i + 1])
            # winners_rating.append(dictVal[i + 1])
            # dict_winners = {winners_team[i]: winners_rating[i] for i in range(len(winners_team))}
            # dict_winners = winners.items()
            # print(dict_winners)

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    while len(teams) > 1:
        teams = simulate_round(teams)
        # print("Team Winners:", teams)
    return teams[0]["team"]


if __name__ == "__main__":
    main()

