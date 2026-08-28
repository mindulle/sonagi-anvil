import pytest
from binary_search_26 import Solution

def test_binary_search_basic():
    sol = Solution()
    assert sol.search([-1,0,3,5,9,12], 9) == 4
    assert sol.search([-1,0,3,5,9,12], 2) == -1

def test_binary_search_edge_cases():
    sol = Solution()
    assert sol.search([], 5) == -1
    assert sol.search([5], 5) == 0
    assert sol.search([5], 2) == -1

def test_binary_search_safe_mid(monkeypatch):
    import binary_search_26 as binary_search
    import ast
    import inspect
    
    # Ensure they don't use (left + right) // 2
    source = inspect.getsource(binary_search.Solution.search)
    assert "(left + right)" not in source, "Use left + (right - left) // 2 to avoid overflow"
