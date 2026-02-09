from utils import add, subtract, to_celsius, to_fahrenheit


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_to_celsius():
    assert to_celsius(32) == 0
    assert to_celsius(212) == 100


def test_to_fahrenheit():
    assert to_fahrenheit(0) == 32
    assert to_fahrenheit(100) == 212
