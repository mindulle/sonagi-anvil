import pytest
from product_of_array_except_self import productExceptSelf

def test_basic():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_with_zero():
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_two_elements():
    assert productExceptSelf([1, 2]) == [2, 1]
