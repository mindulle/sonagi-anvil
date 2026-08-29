import pytest
from combination_sum import Solution

def test_combination_sum():
    sol = Solution()
    
    # Example 1
    assert sorted(sol.combinationSum([2, 3, 6, 7], 7)) == sorted([[2, 2, 3], [7]])
    
    # Example 2
    assert sorted(sol.combinationSum([2, 3, 5], 8)) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    
    # Example 3
    assert sol.combinationSum([2], 1) == []

    # Target smaller than any candidate
    assert sol.combinationSum([5, 6, 7], 3) == []

    # Single element equal to target
    assert sol.combinationSum([7], 7) == [[7]]
