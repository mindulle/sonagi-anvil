# Anki Review - 2026-08-11

## Algorithm Problem Solved
- Problem: 40_maximum_depth_of_binary_tree
- Result: PASS
- Notes/Edge Cases:
    - Empty tree (root = None) correctly returns 0.
    - Single node handles safely and returns 1.
    - Deeply skewed trees might cause `RecursionError` in worst case for DFS. In Python, max recursion depth is ~1000, which corresponds to $O(h)$ space where $h$ is tree height.
    - Time Complexity: O(n) as we visit every node exactly once.
    - Space Complexity: O(h) where h is the height of the tree (for recursion stack). In worst case (skewed tree), O(n).

## Anki Deck Review
- Completed ~15 mins of Spaced Repetition for previous DSA problems (Reverse Linked List, Invert Binary Tree, Number of Islands, etc.).
- The recursive properties of Binary Trees are very intuitive.
- Remembered to test the `root = None` base case reflexively.
