from password import check

def test_valid_password():
    assert check("Abcdefg1") == []

def test_too_short():
    assert "Password too short" in check("Ab1")

def test_missing_capital():
    errors = check("abcdefg1")
    assert "Password must contain atleast 1 capital letter" in errors
    assert "Password must contain atleast 1 number" not in errors

def test_missing_number():
    errors = check("Abcdefgh")
    assert "Password must contain atleast 1 number" in errors
    assert "Password must contain atleast 1 capital letter" not in errors