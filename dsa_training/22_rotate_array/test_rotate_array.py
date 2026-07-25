import pytest
from rotate_array import Solution

def test_rotate():
    sol = Solution()
    
    nums = [1,2,3,4,5,6,7]
    sol.rotate(nums, 3)
    assert nums == [5,6,7,1,2,3,4]
    
    nums = [-1,-100,3,99]
    sol.rotate(nums, 2)
    assert nums == [3,99,-1,-100]
    
    nums = [1]
    sol.rotate(nums, 0)
    assert nums == [1]

    nums = [1, 2]
    sol.rotate(nums, 3)
    assert nums == [2, 1]
