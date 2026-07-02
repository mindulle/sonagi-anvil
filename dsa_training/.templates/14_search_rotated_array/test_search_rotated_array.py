import pytest
from search_rotated_array import search

def test_basic():
    assert search([4,5,6,7,0,1,2], 0) == 4
    assert search([4,5,6,7,0,1,2], 3) == -1
