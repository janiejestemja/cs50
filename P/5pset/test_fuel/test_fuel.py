# Refueling

import pytest
from fuel import convert, gauge

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

    assert convert("0/100") == 0
    assert convert("25/100") == 25
    assert convert("50/100") == 50
    assert convert("75/100") == 75
    assert convert("100/100") == 100

def test_gauge():
    for i in range(1, 100):
        assert gauge(i) == f"{i}%"

    assert gauge(0) == "E"
    assert gauge(100) == "F"