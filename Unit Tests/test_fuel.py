from fuel import converter
from fuel import gauge

def test_converter():
    assert converter(35/100) == 35, 100