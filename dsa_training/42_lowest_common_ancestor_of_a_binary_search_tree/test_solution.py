import pytest
from solution import Solution, TreeNode

def test_lca():
    # Tree:
    #       6
    #     /   \
    #    2     8
    #   / \   / \
    #  0   4 7   9
    #     / \
    #    3   5
    
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    
    sol = Solution()
    
    # p=2, q=8 => LCA=6
    res1 = sol.lowestCommonAncestor(root, root.left, root.right)
    assert res1.val == 6
    
    # p=2, q=4 => LCA=2
    res2 = sol.lowestCommonAncestor(root, root.left, root.left.right)
    assert res2.val == 2

    # p=3, q=5 => LCA=4
    res3 = sol.lowestCommonAncestor(root, root.left.right.left, root.left.right.right)
    assert res3.val == 4
