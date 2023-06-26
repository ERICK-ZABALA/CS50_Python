from seasons import get_birthday
import pytest

def test_valid():

    dateBirth = get_birthday("2021-11-13")
    dateBirth.get_difference()
    dateBirth.convert_numbers_words()
    assert dateBirth.__str__() == "Five hundred twenty-five thousand, six hundred minutes"

    dateBirth = get_birthday("2020-11-13")
    dateBirth.get_difference()
    dateBirth.convert_numbers_words()
    assert dateBirth.__str__() == "One million, fifty-one thousand, two hundred minutes"

    with pytest.raises(ValueError):
        assert get_birthday("January 1, 1999")
