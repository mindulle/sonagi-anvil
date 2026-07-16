import pytest
from coin_change import Solution

def test_coin_change_standard():
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3

def test_coin_change_greedy_trap():
    sol = Solution()
    # Greedy trap: 6 = 4 + 1 + 1 (3 coins) vs DP: 6 = 3 + 3 (2 coins)
    assert sol.coinChange([1, 3, 4], 6) == 2, 'Failed Greedy trap! You likely implemented a Greedy algorithm instead of DP.'
