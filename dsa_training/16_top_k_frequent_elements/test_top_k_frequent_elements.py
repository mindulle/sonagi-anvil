import pytest
from top_k_frequent_elements import topKFrequent

def test_top_k_frequent():
    assert set(topKFrequent([1,1,1,2,2,3], 2)) == {1, 2}
    assert topKFrequent([1], 1) == [1]

def test_empty_or_k_zero():
    assert topKFrequent([], 0) == []
