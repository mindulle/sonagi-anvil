import pytest
from max_depth import Solution, TreeNode

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

def test_max_depth():
    sol = Solution()
    
    # Test case 1: [3,9,20,None,None,15,7]
    root1 = list_to_tree([3, 9, 20, None, None, 15, 7])
    assert sol.maxDepth(root1) == 3
    
    # Test case 2: [1,None,2]
    root2 = list_to_tree([1, None, 2])
    assert sol.maxDepth(root2) == 2
    
    # Test case 3: []
    assert sol.maxDepth(None) == 0
    
    # Test case 4: Single node
    root4 = list_to_tree([0])
    assert sol.maxDepth(root4) == 1
