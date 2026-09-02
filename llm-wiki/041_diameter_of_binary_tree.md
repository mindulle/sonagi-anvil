# Diameter of Binary Tree

## Key Patterns
- Post-order traversal (DFS) is extremely useful when the result of a parent node depends on the subtrees.
- The diameter passing through any node is the sum of the maximum depth of its left and right subtrees.
- The overall diameter is the maximum of all such diameters across all nodes.

## Edge Cases
- Empty tree: Return 0.
- Single node: Return 0 (no edges).
- Skewed tree: The diameter will be exactly the depth of the tree - 1.

## Complexity
- Time: O(N) since each node is visited once.
- Space: O(H) where H is the height of the tree (for the recursion stack). Worst case O(N), average O(log N).
