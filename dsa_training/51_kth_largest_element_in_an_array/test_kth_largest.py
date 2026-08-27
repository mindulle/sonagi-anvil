import pytest
from kth_largest import findKthLargest

def test_findKthLargest():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([-1, -1], 2) == -1
