import pytest
from group_anagrams import Solution

def test_group_anagrams():
    s = Solution()
    # Basic cases
    result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    # The order of groups or elements within groups might vary, 
    # so we should sort for comparison
    sorted_result = sorted([sorted(group) for group in result])
    assert sorted_result == sorted([sorted(["bat"]), sorted(["nat","tan"]), sorted(["ate","eat","tea"])])
    
    # Edge cases
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
    assert s.groupAnagrams(["", ""]) == [["", ""]]
