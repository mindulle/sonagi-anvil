from word_break import wordBreak

def test_word_break():
    assert wordBreak("leetcode", ["leet", "code"]) == True
    assert wordBreak("applepenapple", ["apple", "pen"]) == True
    assert wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
