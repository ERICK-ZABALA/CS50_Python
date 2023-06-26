#!/usr/local/bin/python
from cs50 import get_string


def main():

    text = get_string("Text: ")

    numLetters = count_letters(text)
    numWords = count_words(text)
    numSentences = count_sentences(text)

    print("letters: ", numLetters)
    print("words: ", numWords)
    print("sentences: ", numSentences)

    # formula: index = 0.0588 * (L - 0.296) * (S - 15.8)

    index = 0
    L = 0
    S = 0

    # Important maintain the same variable data in operation.

    L = (float(numLetters) / float(numWords)) * 100
    S = (float(numSentences) / float(numWords)) * 100

    # print(" L:",L)
    # print(" S:",S)

    index = round(((0.0588 * L) - (0.296 * S) - 15.8), 0)
    # print ("index: ",index)
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade ", int(index))

# Count letters function


def count_letters(text):
    i = 0
    count = 0

    for i in range(len(text)):
        if (text[i].islower() or text[i].isupper()):
            count = count + 1
            # printf("numero de letras: %i text: %c\n",count,text1[i]);

    return count


# Count Words function
def count_words(text):
    i = 0
    count = 0

    for i in range(len(text) + 1):
        try:
            if (text[i].isspace() or (text[i] == '\0')):
                count = count + 1
                # printf("numero de letras: %i text: %c\n",count,text1[i]);
        except:
            count = count + 1
    # printf("upos: %i\n", text[strlen(text)+1]);
    return count

# Count Sentences function


def count_sentences(text):
    i = 0
    count = 0

    for i in range(len(text)):
        if ((text[i] == '.') or (text[i] == '!') or (text[i] == '?')):
            count = count + 1
            # printf("numero de letras: %i text: %c\n",count,text1[i]);

    # printf("upos: %i\n", text[strlen(text)+1]);
    return count


if __name__ == "__main__":
    main()
