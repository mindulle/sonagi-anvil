import pytest
from kadanes_negative import Solution

def test_kadane_mixed():
    sol = Solution()
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_kadane_all_negative():
    sol = Solution()
    # If max_sum is initialized to 0, this will wrongly return 0 instead of -1
    assert sol.maxSubArray([-3, -5, -1, -9]) == -1, 'Failed on all-negative array! Did you initialize max_sum to 0?'
