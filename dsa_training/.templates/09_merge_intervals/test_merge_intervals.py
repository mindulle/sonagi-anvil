import pytest
from merge_intervals import merge

def test_basic():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
def test_touching():
    assert merge([[1,4],[4,5]]) == [[1,5]]
