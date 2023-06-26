from fuel import convert, gauge

def main():
     test_division_zero()
     test_division_normal()
     test_value_error()
     
def test_division_zero():
    try:
        convert("2/0")
        assert False
    except ZeroDivisionError:
        assert True
def test_value_error():
    try:
        convert("20/2")
        assert False
    except ValueError:
        assert True


def test_division_normal():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

if __name__ == "__main__":
    main()
