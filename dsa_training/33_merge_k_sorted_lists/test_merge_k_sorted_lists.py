import pytest
from merge_k_sorted_lists import Solution, ListNode

def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def list_to_arr(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

def test_merge_k_lists():
    sol = Solution()
    
    # Normal case
    lists = [create_list([1,4,5]), create_list([1,3,4]), create_list([2,6])]
    result = sol.mergeKLists(lists)
    assert list_to_arr(result) == [1,1,2,3,4,4,5,6]
    
    # Empty case
    assert sol.mergeKLists([]) is None
    
    # List with one empty list
    assert sol.mergeKLists([None]) is None
    
    # All empty
    assert sol.mergeKLists([None, None]) is None
