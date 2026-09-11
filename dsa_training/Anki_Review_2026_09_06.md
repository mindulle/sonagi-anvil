# Anki Review - 2026-09-06

## 1. 58_encode_and_decode_strings
- **Concept:** String manipulation and serialization
- **Review Note:** Use a delimiter like `#` combined with the length of the string to properly encode and avoid collisions with characters inside the strings. Format: `str_len + "#" + string`.
- **Rating:** Hard -> Good

## 2. 59_longest_consecutive_sequence
- **Concept:** Hash Set O(n) lookup
- **Review Note:** Put all elements in a set. Only start counting a sequence if `num - 1` is not in the set, ensuring we only count starting from the first element of each sequence to maintain O(n) total time.
- **Rating:** New -> Good
