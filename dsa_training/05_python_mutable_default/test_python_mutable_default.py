import pytest
from python_mutable_default import Solution

def test_mutable_default():
    sol = Solution()
    res1 = sol.append_item(1)
    res2 = sol.append_item(2)
    assert res1 == [1], 'First call failed'
    assert res2 == [2], 'Second call failed! The list was contaminated by the first call (Mutable Default Argument Bug).' 
