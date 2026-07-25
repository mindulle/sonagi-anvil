import pytest
from valid_palindrome import Solution

def test_isPalindrome():
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    assert sol.isPalindrome("race a car") == False
    assert sol.isPalindrome(" ") == True
