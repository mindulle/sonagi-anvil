import pytest
from coin_change import coinChange

def test_basic():
    assert coinChange([1, 2, 5], 11) == 3
def test_impossible():
    assert coinChange([2], 3) == -1
def test_zero():
    assert coinChange([1], 0) == 0
