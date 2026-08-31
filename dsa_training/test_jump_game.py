import pytest
from jump_game import can_jump

def test_can_jump():
    assert can_jump([2, 3, 1, 1, 4]) == True
    assert can_jump([3, 2, 1, 0, 4]) == False
    assert can_jump([0]) == True
    assert can_jump([2, 0]) == True
    assert can_jump([1, 2, 3]) == True
    assert can_jump([0, 2, 3]) == False
