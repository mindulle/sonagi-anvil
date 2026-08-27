# Anki Review - 2026-07-29

## Algorithm Reviewed
- Sliding Window Maximum (32_sliding_window_maximum)

## Concepts
- Monotonic Deque for Sliding Window Maximum
- Time Complexity: O(n)
- Space Complexity: O(k)

## Notes
- The monotonic deque stores indices, and we keep the values in the deque in decreasing order.
- When a new element comes, remove elements from the back that are smaller than the current element (because they can never be the maximum in the window anymore).
- Remove elements from the front if they are out of the window.
- The maximum is always at the front of the deque.
