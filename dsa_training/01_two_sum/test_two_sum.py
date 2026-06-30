import pytest
from two_sum import two_sum

def test_two_sum_basic():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]

def test_two_sum_different_order():
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]

def test_two_sum_same_elements():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 7) == []

def test_two_sum_empty_or_none():
    assert two_sum([], 9) == []
    assert two_sum(None, 9) == []
