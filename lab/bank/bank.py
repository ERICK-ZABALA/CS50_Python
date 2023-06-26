x = str(input("Greeting: ")).strip().lower()

match x:
    case "hello" | "hello there" | "hello, newman":
        print("$0")
    case "h"|"how you doing?":
        print("$20")
    case _:
        print("$100")