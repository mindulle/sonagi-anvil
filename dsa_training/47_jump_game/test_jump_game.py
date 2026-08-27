import pytest
from jump_game import Solution

def test_can_jump():
    sol = Solution()
    
    # Standard cases
    assert sol.canJump([2, 3, 1, 1, 4]) == True
    assert sol.canJump([3, 2, 1, 0, 4]) == False
    
    # Edge cases
    assert sol.canJump([0]) == True
    assert sol.canJump([0, 2]) == False
    assert sol.canJump([1, 0, 1, 0]) == False
