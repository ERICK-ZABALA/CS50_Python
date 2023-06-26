from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    assert jar.deposit(1) == 11
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert jar.deposit(1) == 11
    assert jar.size == jar.size
    print("Size: ",jar.size)
    print("Cookies in Jar: ",jar.size)

    print("Deposit to jar 13 cookies more ...")

    with pytest.raises(ValueError):
        assert jar.deposit(13)

    print("Cookies in Jar: ",jar.size)
    print("Capacity in Jar: ",jar.capacity)

def test_withdraw():
    jar = Jar()
    assert jar.deposit(1) == 11
    print("Cookies in Jar: ",jar.size)
    print("Capacity in Jar: ",jar.capacity)

    assert jar.withdraw(1) == 12
    print("Cookies in Jar: ",jar.size)
    print("Capacity in Jar: ",jar.capacity)

    with pytest.raises(ValueError):
        assert jar.withdraw(13)




