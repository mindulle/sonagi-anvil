# Anki Review: Group Anagrams

- **Key Insight**: To group anagrams efficiently, we need a canonical representation for each group. Using the character count array (or tuple) of size 26 is O(N*K) time, which is more efficient than sorting each string O(N*K log K).
- **Edge Cases**:
    - Empty list: returns [].
    - List with empty strings: [""] returns [[""]].
    - List with one string: ["a"] returns [["a"]].
- **Complexity**: Time O(N * K) where N is the number of strings and K is the maximum length of a string. Space O(N * K) to store the grouped strings.
