import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("5/6") == 83
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("6/5")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("5//6")
    with pytest.raises(ValueError):
        convert("5./6")
    with pytest.raises(ValueError):
        convert("-5/6")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(83) == "83%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
