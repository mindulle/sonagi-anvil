import pytest
from max_subarray import Solution

def test_max_subarray():
    sol = Solution()
    # Standard cases
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5,4,-1,7,8]) == 23
    
    # Edge case: All negative (should fail with current implementation)
    assert sol.maxSubArray([-3, -5, -2]) == -2
