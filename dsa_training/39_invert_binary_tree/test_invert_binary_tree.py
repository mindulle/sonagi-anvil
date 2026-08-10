import pytest
from invert_binary_tree import Solution, TreeNode

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result

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

def test_invert_binary_tree():
    sol = Solution()
    
    # Test case 1: Normal tree
    root1 = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    inverted1 = sol.invertTree(root1)
    assert tree_to_list(inverted1) == [4, 7, 2, 9, 6, 3, 1]
    
    # Test case 2: Empty tree
    assert sol.invertTree(None) is None
    
    # Test case 3: Single node
    root3 = list_to_tree([1])
    inverted3 = sol.invertTree(root3)
    assert tree_to_list(inverted3) == [1]
    
    # Test case 4: Tree with only left child
    root4 = list_to_tree([1, 2])
    inverted4 = sol.invertTree(root4)
    assert tree_to_list(inverted4) == [1, None, 2]
