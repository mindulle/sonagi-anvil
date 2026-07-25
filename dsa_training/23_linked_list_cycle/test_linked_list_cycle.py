import pytest
from linked_list_cycle import hasCycle, ListNode

def test_has_cycle_true():
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # cycle
    assert hasCycle(node1) is True

def test_has_cycle_false():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert hasCycle(node1) is False

def test_has_cycle_empty():
    assert hasCycle(None) is False
