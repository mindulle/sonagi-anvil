import pytest
from course_schedule import Solution

def test_course_schedule():
    sol = Solution()
    # Standard cases
    assert sol.canFinish(2, [[1,0]]) == True
    assert sol.canFinish(2, [[1,0],[0,1]]) == False
    assert sol.canFinish(5, [[1,0],[2,1],[3,2],[4,3]]) == True
