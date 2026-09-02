# Anki Review - 2026-08-10

## Algorithm Problem Solved
- Problem: 39_invert_binary_tree
- Result: PASS
- Notes/Edge Cases:
    - Empty tree (root = None) correctly returns None.
    - Single node handles safely without recursion errors.
    - Swapping should happen before or after recursive calls (either works, but typically preorder swap is easiest).
    - Time Complexity: O(n) as we visit every node exactly once.
    - Space Complexity: O(h) where h is the height of the tree (for recursion stack). In worst case (skewed tree), O(n).

## Anki Deck Review
- Completed ~10 mins of Spaced Repetition for previous DSA problems (Reverse Linked List, Two Sum, etc.).
- Muscle memory for linked list pointer swapping and basic binary tree recursion is solidifying.
- Need to keep reinforcing Sliding Window patterns next time.
