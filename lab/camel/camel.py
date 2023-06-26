word = str(input("camelCase: ").strip())

print("snake_case: ", end="")

for i in range (len(word)):
    if (word[i].islower()):
        print(word[i], end="")
    elif (word[i].isupper()):
        word_modified = word[i].lower()
        print("_" + word_modified, end="")
        
print("")
