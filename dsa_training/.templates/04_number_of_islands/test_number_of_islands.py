import pytest
from number_of_islands import Solution

def test_number_of_islands():
    sol = Solution()
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert sol.numIslands(grid1) == 1

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert sol.numIslands(grid2) == 3

    assert sol.numIslands([]) == 0
