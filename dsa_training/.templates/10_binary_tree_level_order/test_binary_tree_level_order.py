import pytest
from binary_tree_level_order import levelOrder, TreeNode

def test_basic():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert levelOrder(root) == [[3], [9, 20], [15, 7]]
