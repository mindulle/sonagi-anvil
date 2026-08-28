# Anki Review 2026-08-02

## Algorithm Practice
- **Problem**: 35. Valid Anagram
- **Key Concepts**: Hash Table, Frequency Counting
- **Notes**: 
    - Given two strings, return true if they are anagrams.
    - Check lengths first: if not equal, return `False`.
    - Use a hash map (dictionary) to count character occurrences in `s`, then decrement using `t`.
    - Time Complexity: O(N).
    - Space Complexity: O(1) if character set is fixed (e.g., lowercase English), or O(K) where K is number of unique characters.

## Anki Cards to Add
1. Q: How to check if two strings are anagrams?
   A: First, check if lengths are equal. Then, create a character frequency count for one string and subtract counts using the second string. If any count becomes negative or char not found, return `False`.

2. Q: What is the time complexity of the hash map approach for Valid Anagram?
   A: O(N), where N is the length of the string, as we traverse both strings once.
