from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            # Use tuple of counts as key for O(N*K) where N is number of strs, K is max length of string
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())
