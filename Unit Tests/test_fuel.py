from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("35/100") == (35, 100)

