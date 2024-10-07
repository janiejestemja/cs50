# Testing my twttr

from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("sOmEthIng :)") == "smthng :)"
    assert shorten("'October' 31, 1749") == "'ctbr' 31, 1749"