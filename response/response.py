
from validator_collection import validators, errors

def main():
    print(verify(input("What's your email address? ").strip()))

def verify(s):

    try:
        email = validators.email(s)

        return f"Valid"
    # Will raise an EmptyValueError
    except errors.EmptyValueError:
        # Handling logic goes here
        return "Invalid"

    except errors.InvalidEmailError:
        # More handlign logic goes here
        return "Invalid"
    except ValueError:
        # handle the error
        return "Invalid"


if __name__ == '__main__':
    main()