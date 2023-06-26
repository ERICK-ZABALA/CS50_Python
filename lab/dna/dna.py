#!/usr/local/bin/python

import csv
import sys

name = []
agatc = []
ttttttct = []
aatg = []
tctag = []
gata = []
tatc = []
gaaa = []
tctg = []

match = {'AGATC': 0,
         'TTTTTTCT': 0,
         'AATG': 0,
         'TCTAG': 0,
         'GATA': 0,
         'TATC': 0,
         'GAAA': 0,
         'TCTG': 0
         }


def main():

    # TODO: Check for command-line usage
    try:

        if len(sys.argv) == 3:
            # CLI: python dna.py databases/large.csv sequences/5.txt
            print("", end="")
        elif len(sys.argv) == 2:
            print("Usage: python dna.py data.csv sequence.txt")
        elif len(sys.argv) == 1:
            print("Usage: python dna.py data.csv sequence.txt")

    except ValueError:
        print("Usage: python dna.py data.csv sequence.txt - Sintaxis Error!!!")
        exit()

    # print(sys.argv[1])
    label = read_database(sys.argv[1])

    sequence = read_sequence(sys.argv[2])

    longest_match_str(sequence, label)

    profile_match()

    # TODO: Read database file into a variable


def read_database(database):

    counter = {'count': 0}

    # print(database)
    if database == "databases/large.csv":
        with open(database, "r") as file:
            reader = csv.DictReader(file)
            # print(type(reader))
            for row in reader:

                name_list = row["name"]
                agatc_list = int(row["AGATC"])
                ttttttct_list = int(row["TTTTTTCT"])
                aatg_list = int(row["AATG"])
                tctag_list = int(row["TCTAG"])
                gata_list = int(row["GATA"])
                tatc_list = int(row["TATC"])
                gaaa_list = int(row["GAAA"])
                tctg_list = int(row["TCTG"])

                name.append(name_list)
                agatc.append(agatc_list)
                ttttttct.append(ttttttct_list)
                aatg.append(aatg_list)
                tctag.append(tctag_list)
                gata.append(gata_list)
                tatc.append(tatc_list)
                gaaa.append(gaaa_list)
                tctg.append(tctg_list)

                counter["count"] = counter["count"] + 1
            label = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
            return label

    if database == "databases/small.csv":
        with open(database, "r") as file:
            reader = csv.DictReader(file)
            # print(type(reader))
            for row in reader:

                name_list = row["name"]
                agatc_list = int(row["AGATC"])
                aatg_list = int(row["AATG"])
                tatc_list = int(row["TATC"])

                name.append(name_list)
                agatc.append(agatc_list)
                aatg.append(aatg_list)
                tatc.append(tatc_list)

                counter["count"] = counter["count"] + 1
            label = ["AGATC", "AATG", "TATC"]
            return label

    # TODO: Read DNA sequence file into a variable


def read_sequence(sequence):
    # print(sequence)
    with open(sequence, "r") as file:
        reader = csv.reader(file)
        # print(type(reader))
        for row in reader:
            sequence = row[0]
    return sequence

    # TODO: Find longest match of each STR in DNA sequence


def longest_match_str(sequence, label):

    count = 0
    num = len(label)
    for i in range(num):
        value = longest_match(sequence, label[i])
        match[label[i]] = value
        count = count + 1
       # print("L: ",label[i])
       # print("value:",value)

    # TODO: Check database for matching profiles


def profile_match():

    # print(match)
    valA = []
    valA = match ["AGATC"]
    valB = []
    valB = match ["TTTTTTCT"]
    valC = []
    valC = match ["AATG"]
    valD = []
    valD = match ["TCTAG"]
    valE = []
    valE = match ["GATA"]
    valF = []
    valF = match ["TATC"]
    valG = []
    valG = match ["GAAA"]
    valH = []
    valH = match ["TCTG"]
    # agatc = [x.x.x.x.x.x]
    num = len(agatc)

    if num < 4:
        for i in range(num):

            if valA == agatc[i] and valB == 0 and valC == aatg[i] and valD == 0 and valE == 0 and valF == tatc[i] and valG == 0 and valH == 0:
                print(name[i], end="\n")
                return 0

            elif (valA != agatc[i] or valC != aatg[i] or valF != tatc[i]) and (i == 2):
                print('No match', end="\n")
                return 0

    for i in range(num):

        if valA == agatc[i] and valB == ttttttct[i] and valC == aatg[i] and valD == tctag[i] and valE == gata[i] and valF == tatc[i] and valG == gaaa[i] and valH == tctg[i]:
            # print("AGATC: ", agatc[i])
            print(name[i], end="\n")
            return 0

        elif valA != agatc[i] and valB != ttttttct[i] and valC != aatg[i] and valD != tctag[i] and valE != gata[i] and valF != tatc[i] and valG != gaaa[i] and valH != tctg[i] and i == 22:
            print('No match', end="\n")
            return 0


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
