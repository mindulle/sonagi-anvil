# 44. Implement Trie (Prefix Tree)

## Notes & Edge Cases
- **Pattern**: A `TrieNode` typically has a hash map or array of length 26 to store references to child nodes.
- **is_end_of_word**: Essential to distinguish words from mere prefixes.
- **Python optimization**: Using a dictionary for `children` makes it flexible to handle any character without calculating array indices, at a slight memory overhead compared to an array of size 26.
