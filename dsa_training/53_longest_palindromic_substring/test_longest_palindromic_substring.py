from longest_palindromic_substring import longest_palindrome

def test_longest_palindrome():
    # "babad" -> "bab" or "aba"
    res1 = longest_palindrome("babad")
    assert res1 in ["bab", "aba"]
    
    # "cbbd" -> "bb"
    assert longest_palindrome("cbbd") == "bb"
    
    # "a" -> "a"
    assert longest_palindrome("a") == "a"
    
    # "ac" -> "a" or "c"
    res2 = longest_palindrome("ac")
    assert len(res2) == 1
    assert res2 in ["a", "c"]
    
    # empty string
    assert longest_palindrome("") == ""
