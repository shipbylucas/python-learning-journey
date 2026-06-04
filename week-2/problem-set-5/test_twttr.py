from twttr import shorten

def test_upper():
    assert shorten("TwIttEr") == "Twttr"
    assert shorten("HOAng") == "Hng"


def test_lower():
    assert shorten("hihi") == "hh"
    assert shorten("hoho") == "hh"

def test_num():
    assert shorten("h53") == "h53"
    assert shorten("2h4") == "2h4"

def test_punc():
    assert shorten("hi,ha") == "h,h"
    assert shorten("l.ohh") == "l.hh"
