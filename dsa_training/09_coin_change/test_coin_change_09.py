import pytest
from coin_change_09 import coinChange

def test_coin_change():
    assert coinChange([1, 2, 5], 11) == 3
    assert coinChange([2], 3) == -1
    assert coinChange([1], 0) == 0
    assert coinChange([1, 3, 4], 6) == 2  # The case mentioned in content/009_coin_change_greedy_bug.md
    assert coinChange([], 5) == -1

if __name__ == "__main__":
    pytest.main([__file__])
