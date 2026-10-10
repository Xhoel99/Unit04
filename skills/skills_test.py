""" Exercise 2 """

from skills import is_speeding

def test_is_speeding_true():
    assert is_speeding(75, 65) is True

def test_is_speeding_false():
    assert is_speeding(45, 65) is False