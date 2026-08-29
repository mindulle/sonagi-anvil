# Anki Review 2026-08-04

## Algorithm Practice
- **Problem**: 35. Valid Anagram
- **Key Concepts**: Hash Map / Frequency Counting
- **Notes**:
    - For strings s and t, compare their character frequency counts.
    - If `len(s) != len(t)`, they cannot be anagrams.
    - If using only lowercase English letters, an array of size 26 is optimal.
    - If strings contain Unicode, a hash map (dictionary) is necessary.
    - Time complexity: O(n), Space complexity: O(1) if character set is fixed, otherwise O(n).

## Anki Cards to Add
1. Q: What are the trade-offs between using a hash map and a fixed-size array for tracking character counts in anagram problems?
   A: Fixed-size array (e.g., size 26) is faster and uses constant space (O(1)) if character set is fixed (e.g., lowercase English letters). Hash map is more flexible and handles arbitrary characters (Unicode) but has slightly higher overhead and O(K) space complexity where K is number of unique characters.
