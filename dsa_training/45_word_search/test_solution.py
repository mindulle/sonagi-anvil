import pytest
from solution import Solution

def test_exist():
    sol = Solution()
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    assert sol.exist(board, "ABCCED") == True
    assert sol.exist(board, "SEE") == True
    assert sol.exist(board, "ABCB") == False
    
def test_exist_single_char():
    sol = Solution()
    board = [["a"]]
    assert sol.exist(board, "a") == True
    assert sol.exist(board, "b") == False

def test_exist_empty_board():
    sol = Solution()
    assert sol.exist([], "a") == False
    assert sol.exist([[]], "a") == False
