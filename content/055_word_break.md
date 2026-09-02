# Prompt
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Buggy Code
```python
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    
    def dfs(s):
        if not s:
            return True
        
        for i in range(1, len(s) + 1):
            if s[:i] in word_set and dfs(s[i:]):
                return True
        return False
        
    return dfs(s)
```

# Solution
The buggy code uses simple recursion without memoization (DFS). While logically correct, this approach leads to a Time Limit Exceeded (TLE) error for long strings or strings with repeating patterns. The time complexity of this unoptimized recursion is $O(2^N)$ in the worst case.

We can optimize this using Dynamic Programming.
We create a boolean DP array of size `len(s) + 1` where `dp[i]` represents whether the prefix of `s` of length `i` can be segmented into dictionary words. For each length `i`, we check if there's any length `j < i` such that `dp[j]` is True and the substring `s[j:i]` is in the dictionary. If so, we set `dp[i] = True` and break the inner loop.

```python
from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
                
    return dp[len(s)]
```

- **Time Complexity:** $O(N^2)$, where $N$ is the length of the string $s$. The two nested loops iterate $N$ times each. Substring extraction `s[j:i]` can take $O(N)$ time, but string slicing is generally fast, and maximum word length could be bounded. In worst case it's $O(N^3)$ considering slicing, but usually $O(N^2)$ assuming max word length is a small constant.
- **Space Complexity:** $O(N)$ for the `dp` array.
