import pytest
from longest_palindromic_substring import longestPalindrome

def test_odd_length_palindrome():
    assert longestPalindrome("babad") in ["bab", "aba"]

def test_even_length_palindrome():
    assert longestPalindrome("cbbd") == "bb"

def test_single_character():
    assert longestPalindrome("a") == "a"

def test_two_characters_not_palindrome():
    assert longestPalindrome("ac") in ["a", "c"]

def test_all_same_characters():
    assert longestPalindrome("aaaa") == "aaaa"

def test_long_string():
    assert longestPalindrome("forgeeksskeegfor") == "geeksskeeg"
