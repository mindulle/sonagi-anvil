# Anki Review - 2026-09-02

## Today's Problem: Word Break (LeetCode 139)
- **Concept:** Dynamic Programming
- **Key Idea:** Create a boolean DP array of size `len(s) + 1` where `dp[i]` represents whether the prefix of `s` of length `i` can be segmented into dictionary words. For each length `i`, check if there's any length `j < i` such that `dp[j]` is True and the substring `s[j:i]` is in the dictionary.
- **Complexity:** Time O(N^2), Space O(N) where N is the length of `s`.

## Spaced Repetition (Past Problems)
- Reviewed Binary Search boundaries.
- Reviewed sliding window maximum edge cases.
