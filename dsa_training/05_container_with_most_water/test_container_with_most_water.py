import pytest
from container_with_most_water import Solution

def test_max_area():
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16
    assert sol.maxArea([1, 2, 1]) == 2
