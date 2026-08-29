import pytest
from sliding_window_maximum import Solution

def test_max_sliding_window():
    sol = Solution()
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert sol.maxSlidingWindow([9, 11], 2) == [11]
    assert sol.maxSlidingWindow([4, -2], 2) == [4]
