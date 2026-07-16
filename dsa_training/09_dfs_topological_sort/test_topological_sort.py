import pytest
from topological_sort import Solution

def test_no_cycle():
    sol = Solution()
    assert sol.canFinish(2, [[1,0]]) == True

def test_cycle():
    sol = Solution()
    assert sol.canFinish(2, [[1,0],[0,1]]) == False

def test_tle_trap():
    sol = Solution()
    # A graph where nodes point to an already validated safe node.
    # If safe nodes aren't memoized as state '2', this will cause exponential re-evaluation.
    # 0 -> 1 -> 2.  3 -> 1. 
    assert sol.canFinish(4, [[1,0], [2,1], [1,3]]) == True
