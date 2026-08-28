class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity: O(H) where H is the height of the tree. In the worst case (skewed tree), it can be O(N).
        Space Complexity: O(1) as we are using iterative approach, no call stack overhead.
        """
        current = root
        
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # We found the split point, i.e. the LCA node.
                return current
        
        return None
