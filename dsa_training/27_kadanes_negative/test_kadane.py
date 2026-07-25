import pytest
from kadane import Solution

def test_kadane_mixed():
    sol = Solution()
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sol.maxSubArray([5,4,-1,7,8]) == 23

def test_kadane_all_negative():
    sol = Solution()
    # A naive implementation setting max_sum = 0 will fail this test
    assert sol.maxSubArray([-5, -2, -9, -1]) == -1
    assert sol.maxSubArray([-3]) == -3

def test_kadane_edge():
    sol = Solution()
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([0]) == 0
