import pytest
from binary_search import Solution

def test_binary_search():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert sol.search([], 5) == -1
    assert sol.search([5], 5) == 0
    assert sol.search([1, 2, 3, 4, 5], 1) == 0
    assert sol.search([1, 2, 3, 4, 5], 5) == 4

def test_large_array():
    sol = Solution()
    nums = list(range(1000000))
    assert sol.search(nums, 999999) == 999999
    assert sol.search(nums, -1) == -1
