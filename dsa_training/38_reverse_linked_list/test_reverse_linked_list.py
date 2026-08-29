from reverse_linked_list import Solution, ListNode

def test_reverse_list():
    sol = Solution()
    
    # Test case 1: 1->2->3->4->5->None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = sol.reverseList(head)
    
    # Expected: 5->4->3->2->1->None
    curr = reversed_head
    expected = [5, 4, 3, 2, 1]
    for val in expected:
        assert curr is not None
        assert curr.val == val
        curr = curr.next
    assert curr is None

    # Test case 2: 1->2->None
    head = ListNode(1, ListNode(2))
    reversed_head = sol.reverseList(head)
    # Expected: 2->1->None
    assert reversed_head.val == 2
    assert reversed_head.next.val == 1
    
    # Test case 3: None
    assert sol.reverseList(None) is None
