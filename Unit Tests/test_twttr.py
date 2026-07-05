from twttr import shorten


def test_lowercase():
    assert shorten("omer") == "mr"


def test_uppercase():
    assert shorten("OMER") == "MR"


def test_mixed_case():
    assert shorten("OmEr") == "mr"


def test_all_vowels():
    assert shorten("aeiou") == ""


def test_empty_string():
    assert shorten("") == ""