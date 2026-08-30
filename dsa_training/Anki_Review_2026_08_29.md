# Anki Review 2026-08-29

## Spaced Repetition (Daily Review)
- **Top K Frequent Elements**: Min-Heap (`heapq` in Python). Time: O(N log K), Space: O(N).
- **Longest Substring Without Repeating Characters**: Sliding Window + Hash Map. Keep track of the last seen index of each character to efficiently update `left` pointer. Time: O(N), Space: O(min(N, M)) where M is charset size.
- **Merge Intervals**: Sort by start time. Iterate and if `current.start <= merged[-1].end`, update `merged[-1].end = max(...)`. Time: O(N log N), Space: O(N).
- **Longest Palindromic Substring**: Expand Around Center technique. Time: O(N^2), Space: O(1).
