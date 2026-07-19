from password import check

def test_valid_password():
    assert check("Abcdefg1") == True

def test_too_short():
    assert check("Ab1") == "Password too short"

def test_missing_number():
    assert check("Abcdefgh") == "Password must contain atleast 1 number"