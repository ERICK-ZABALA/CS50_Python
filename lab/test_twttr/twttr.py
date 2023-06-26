def main():
    word = str(input("Input: ").strip())
    new_word = shorten(word)
    print("Output:", new_word)

def shorten(word):
    # print(word)
    new_word = []
    for i in range(len(word)):
        match word[i]:
            case 'a' | 'e' | 'i' | 'o' | 'u' |'A' | 'E' | 'I' | 'O' | 'U':
                word[i].replace(word[i],"")
            case _:
                word[i]
                new_word.append(word[i])

    return ''.join(new_word)

if __name__ == "__main__":
    main()

