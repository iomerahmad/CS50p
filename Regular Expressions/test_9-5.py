from job import convert
import pytest


def test_standard_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_mixed_minutes():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_overnight():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


def test_noon_and_midnight():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 a.m. to 5:00 p.m.")


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")


def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")