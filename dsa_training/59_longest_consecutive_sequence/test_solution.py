import pytest
from solution import longest_consecutive

def test_longest_consecutive_basic():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

def test_longest_consecutive_empty():
    assert longest_consecutive([]) == 0

def test_longest_consecutive_duplicates():
    assert longest_consecutive([1, 2, 0, 1]) == 3

def test_longest_consecutive_negative():
    assert longest_consecutive([-1, -2, -3, 0, 1]) == 5

def test_longest_consecutive_single_element():
    assert longest_consecutive([10]) == 1
