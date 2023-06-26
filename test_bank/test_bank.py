from bank import value

def main():
    test_greeting_hello()
    test_greeting_hyd()
    test_greeting_default()

def test_greeting_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
def test_greeting_hyd():
    assert value("h") == 20
    assert value("how are you") == 20
def test_greeting_default():
    assert value("123") == 100
    assert value("cisco") == 100
    assert value("cs50") == 100

