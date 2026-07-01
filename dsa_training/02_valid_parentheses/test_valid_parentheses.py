import pytest
from valid_parentheses import Solution

def test_valid_parentheses():
    sol = Solution()
    assert sol.isValid("()") == True
    assert sol.isValid("()[]{}") == True
    assert sol.isValid("(]") == False
    assert sol.isValid("([)]") == False
    assert sol.isValid("{[]}") == True
    assert sol.isValid("") == True
    assert sol.isValid("[") == False
