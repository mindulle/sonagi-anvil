import pytest
from mutable_default import Solution

def test_mutable_default():
    sol = Solution()
    # First call: should return [1]
    res1 = sol.append_to_list(1)
    assert res1 == [1]
    
    # Second call: should return [2], not [1, 2]
    res2 = sol.append_to_list(2)
    assert res2 == [2]
    
    # Third call with explicit list
    res3 = sol.append_to_list(3, [])
    assert res3 == [3]
