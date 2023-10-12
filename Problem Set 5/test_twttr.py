from twttr import shorten
import pytest

def main():
    test_case()
    test_numbers()
    test_punctuation()

def test_case():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"


def test_numbers():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("!?.,") == "!?.,"