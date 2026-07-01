import pytest
from two_sum import Solution

def test_two_sum_basic():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]

def test_two_sum_not_found():
    sol = Solution()
    assert sol.twoSum([1, 2], 10) == []
