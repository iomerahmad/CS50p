from fuel import convert
from fuel import gauge

def test_gauge_edges():
    assert gauge(0, 1) == 0
    assert gauge(99, 100) == 99

