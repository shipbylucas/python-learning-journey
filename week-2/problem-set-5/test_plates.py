from plates import is_valid

def test_2letter():
    assert is_valid("HI50") == True
    assert is_valid("H50") == False
    assert is_valid("50") == False
    assert is_valid("5HI0") == False
    assert is_valid("50HI") == False

def test_len():
    assert is_valid("HI5099") == True
    assert is_valid("I5") == False
    assert is_valid("5") == False
    assert is_valid("HI5099777") == False

def test_numpo():
    assert is_valid("HI50") == True
    assert is_valid("HIK50") == True
    assert is_valid("HI50K") == False
    assert is_valid("HI5K0") == False
    assert is_valid("HI05") == False

def test_specchar():
    assert is_valid("HI50") == True
    assert is_valid("HI50,") == False
    assert is_valid("HI.50") == False
    assert is_valid("HI5_0") == False
