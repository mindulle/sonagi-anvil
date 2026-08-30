import pytest
from longest_increasing_subsequence import Solution

def test_lengthOfLIS():
    sol = Solution()
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert sol.lengthOfLIS([]) == 0
    assert sol.lengthOfLIS([1]) == 1
