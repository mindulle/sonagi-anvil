import pytest
from find_duplicate import findDuplicate

def test_find_duplicate():
    assert findDuplicate([1,3,4,2,2]) == 2
    assert findDuplicate([3,1,3,4,2]) == 3
    assert findDuplicate([2,2,2,2,2]) == 2
