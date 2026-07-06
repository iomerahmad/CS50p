from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("OMER12") == True
    assert is_valid("AA") == True
    assert is_valid("ABC123") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_first_two_letters():
    assert is_valid("1ABC") == False
    assert is_valid("A1BC") == False


def test_first_number_not_zero():
    assert is_valid("CS05") == False
    assert is_valid("AB012") == False


def test_numbers_at_end():
    assert is_valid("AAA22A") == False
    assert is_valid("CS5P") == False
    assert is_valid("AB12CD") == False


def test_alphanumeric_only():
    assert is_valid("PI.3") == False
    assert is_valid("CS 50") == False
    assert is_valid("AA-11") == False