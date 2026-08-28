from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(N) where N is the number of nodes in the tree, 
        as we visit every node once.
        Space Complexity: O(H) where H is the height of the tree for the recursion stack.
        In the worst case (skewed tree) it is O(N), for a balanced tree it's O(log N).
        """
        self.diameter = 0
        
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # The diameter passing through this node
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the depth of this subtree
            return max(left_depth, right_depth) + 1
            
        depth(root)
        return self.diameter
