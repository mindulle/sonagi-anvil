import pytest
from valid_anagram import Solution

@pytest.fixture
def solution():
    return Solution()

def test_anagram(solution):
    assert solution.isAnagram("anagram", "nagaram") == True

def test_not_anagram(solution):
    assert solution.isAnagram("rat", "car") == False

def test_different_lengths(solution):
    assert solution.isAnagram("a", "ab") == False

def test_empty_strings(solution):
    assert solution.isAnagram("", "") == True

def test_single_characters(solution):
    assert solution.isAnagram("a", "a") == True
    assert solution.isAnagram("a", "b") == False
