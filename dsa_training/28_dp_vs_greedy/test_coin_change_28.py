import pytest
from coin_change_28 import Solution

def test_coin_change_basic():
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3

def test_coin_change_unreachable():
    sol = Solution()
    assert sol.coinChange([2], 3) == -1

def test_coin_change_dp_required():
    sol = Solution()
    # Greedy would choose 4 + 1 + 1 = 3 coins.
    # DP should find 3 + 3 = 2 coins.
    assert sol.coinChange([1, 3, 4], 6) == 2

def test_coin_change_zero():
    sol = Solution()
    assert sol.coinChange([1], 0) == 0
