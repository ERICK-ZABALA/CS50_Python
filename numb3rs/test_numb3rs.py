
from numb3rs import validate

def main():
    test_validate_True()
    test_validate_False()


def test_validate_True():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1.") == False



def test_validate_False():
    assert validate(r"512.512.512.512") == False
    assert validate(r"1") == False
    assert validate(r"cat") == False
    assert validate(r"1000.100.1.1") == False
    assert validate(r"1.1000.100.1") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"1.1.1.512") == False




if __name__=='__main__':
    main()