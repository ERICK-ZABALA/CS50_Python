x = str(input("What is the Answer to the Great Question of Life, the Universe and Everything? ")).strip().lower()

match x:
    case "42" | "forty-two" | "forty two":
        print("Yes", end="\n")
    case _:
        print("No", end="\n")

