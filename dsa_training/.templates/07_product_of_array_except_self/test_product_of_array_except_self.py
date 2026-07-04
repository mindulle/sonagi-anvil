import pytest
from product_of_array_except_self import productExceptSelf

def test_basic_array():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_array_with_zero():
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_array_with_multiple_zeros():
    assert productExceptSelf([0, 1, 0, 4]) == [0, 0, 0, 0]

def test_array_with_two_elements():
    assert productExceptSelf([3, 4]) == [4, 3]

def test_all_negative_numbers():
    assert productExceptSelf([-2, -3, -4]) == [12, 8, 6]
