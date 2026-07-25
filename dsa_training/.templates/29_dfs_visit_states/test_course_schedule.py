import pytest
from course_schedule import Solution

def test_can_finish_basic():
    sol = Solution()
    assert sol.canFinish(2, [[1,0]]) == True
    assert sol.canFinish(2, [[1,0], [0,1]]) == False

def test_can_finish_disconnected_cycle():
    sol = Solution()
    # Cycle in a disconnected component
    assert sol.canFinish(4, [[1,0], [2,3], [3,2]]) == False

def test_can_finish_complex():
    sol = Solution()
    assert sol.canFinish(5, [[1,0],[2,1],[3,2],[4,3]]) == True
    # Long cycle
    assert sol.canFinish(5, [[1,0],[2,1],[3,2],[4,3],[0,4]]) == False
