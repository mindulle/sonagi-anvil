import pytest
from diameter_of_binary_tree import Solution, TreeNode

def test_diameter_of_binary_tree():
    sol = Solution()
    
    # Example 1
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert sol.diameterOfBinaryTree(root) == 3
    
    # Example 2
    #     1
    #    /
    #   2
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert sol.diameterOfBinaryTree(root) == 1
    
    # Edge case: Empty tree
    assert sol.diameterOfBinaryTree(None) == 0

    # Edge case: Single node
    assert sol.diameterOfBinaryTree(TreeNode(1)) == 0
