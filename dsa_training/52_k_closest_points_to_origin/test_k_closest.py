import pytest
from k_closest import Solution

def test_k_closest():
    sol = Solution()
    
    # Test case 1
    assert sorted(sol.kClosest([[1,3],[-2,2]], 1)) == [[-2,2]]
    
    # Test case 2
    res = sol.kClosest([[3,3],[5,-1],[-2,4]], 2)
    assert sorted(res) == sorted([[3,3],[-2,4]])
    
    # Test case 3: points with same distance
    res = sol.kClosest([[1,1],[-1,-1]], 1)
    assert len(res) == 1
    assert res[0] in [[1,1],[-1,-1]]
