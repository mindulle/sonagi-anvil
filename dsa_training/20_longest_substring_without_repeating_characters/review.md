# Anki Review: Longest Substring Without Repeating Characters

- **Key Insight**: Sliding Window technique using a HashMap to store the last seen index of each character.
- **Edge Cases**:
    - Empty string: returns 0.
    - String with all unique characters: returns string length.
    - String with all same characters: returns 1.
    - String with spaces: handles spaces correctly as characters.
- **Complexity**: Time O(N), Space O(min(N, M)) where M is the character set size.
