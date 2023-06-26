def main():
    greeting = str(input("Greeting: "))
    message = value(greeting)
    print(f"${message}")

def value(greeting):
    greeting = greeting.strip().lower()

    if greeting[0:5] == "hello":
        return 0
    elif greeting == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
