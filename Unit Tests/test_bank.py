from bank import value


def test_hello():
    assert value("hello") == "$0"
    assert value("hello there") == "$0"


def test_starts_with_h():
    assert value("hi") == "$20"
    assert value("howdy") == "$20"


def test_other():
    assert value("bonjour") == "$100"
    assert value("good morning") == "$100"


def test_case_sensitivity():
    # value() itself is case-sensitive — lowercasing happens in main(), not here
    assert value("HELLO") == "$100"
    assert value("Hi") == "$100"
