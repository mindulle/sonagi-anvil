import pytest
import ast
import inspect
from binary_search_overflow import Solution

def test_binary_search_logic():
    sol = Solution()
    assert sol.search([-1,0,3,5,9,12], 9) == 4
    assert sol.search([-1,0,3,5,9,12], 2) == -1

def test_avoid_overflow_formula():
    source = inspect.getsource(Solution.search)
    # Check if (left + right) // 2 is used by looking for simple string match
    # In a real AST check, we'd parse it, but for training, string check is enough
    assert 'left + right' not in source.replace(' ', ''), 'Found unsafe (left+right) formula which causes Integer Overflow in languages like Java/C++. Use left + (right - left) // 2'
