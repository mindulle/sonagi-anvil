import pytest
from two_sum import Solution

def test_two_sum():
    sol = Solution()
    # Standard cases
    assert sorted(sol.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(sol.twoSum([3, 3], 6)) == [0, 1]
    
    # Edge cases
    assert sol.twoSum([], 9) == []
    assert sol.twoSum([1], 1) == []
