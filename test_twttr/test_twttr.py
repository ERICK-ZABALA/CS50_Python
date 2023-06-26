from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("cs50") == "cs50"
    assert shorten("CS50") == "CS50"
    assert shorten("cs") == "cs"
    assert shorten(".,?") == ".,?"
    assert shorten("21234") == "21234"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("W123a") == "W123"
    assert shorten('ELON') == 'LN'

if __name__ == "__main__":
    main()

