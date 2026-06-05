from bank import value

def test_hello():
    assert value("HELLO, David") == 0
    assert value("hello DAVID") == 0
    assert value("he,llo david") == 20
    assert value("hello1234") == 0
    assert value("hELLO hehe") ==0

def test_h():
    assert value("HEYY hey") == 20
    assert value("hey hello") == 20
    assert value("h123") == 20

def test_none():
    assert value("123") == 100
    assert value("my name is David") == 100
    assert value("WHATS WRONG?") == 100
