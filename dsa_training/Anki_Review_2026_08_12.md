# Anki Review - 2026-08-12

## Algorithm Problem Solved
- Problem: 41_diameter_of_binary_tree
- Result: PASS
- Notes/Edge Cases:
    - Empty tree (root = None) correctly returns 0.
    - Single node handles safely and returns 0.
    - Time Complexity: O(N) as we visit every node exactly once.
    - Space Complexity: O(H) where H is the height of the tree (for recursion stack). In worst case (skewed tree), O(N).
    - Post-order traversal where we calculate left and right depths, updating global diameter while returning max depth to parent.

## Anki Deck Review
- Completed 10 mins of Spaced Repetition for previous DSA problems (Maximum Depth of Binary Tree, Reverse Linked List, Invert Binary Tree).
- Reinforced tree traversal techniques (DFS vs BFS) and space complexity analysis based on call stack size (O(H)).
- Key takeaway: The diameter isn't always passing through the root! Global variable or nonlocal is needed to track the max across all subtrees.
