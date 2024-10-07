from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(capacity=-1)
        jar.capacity = -1

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(10)
    assert jar.size == jar.capacity

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)
        jar.withdraw(1)
    jar.deposit(12)
    jar.withdraw(2) 
    assert jar.size == 10
    jar.withdraw(jar.size) 
    assert jar.size == 0
