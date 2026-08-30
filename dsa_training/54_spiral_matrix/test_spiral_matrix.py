import pytest
from spiral_matrix import Solution

def test_spiral_order():
    sol = Solution()
    assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert sol.spiralOrder([]) == []
    assert sol.spiralOrder([[1]]) == [1]
    assert sol.spiralOrder([[3],[2]]) == [3,2]
