word = str(input("word: ").strip())
# print(word)
for i in range(len(word)):
    match word[i]:
        case 'a' | 'e' | 'i' | 'o' | 'u' |'A' | 'E' | 'I' | 'O' | 'U':
            word[i].replace(word[i],"")
        case _:
            print(word[i], end ="")
print()




