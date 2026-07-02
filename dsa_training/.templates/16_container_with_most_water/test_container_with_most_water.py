import pytest
from container_with_most_water import maxArea

def test_basic():
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1
