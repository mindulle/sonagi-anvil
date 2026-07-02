import pytest
from word_search import exist

def test_basic():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "ABCCED") == True
    assert exist(board, "SEE") == True
    assert exist(board, "ABCB") == False
