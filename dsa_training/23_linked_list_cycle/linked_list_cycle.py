# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    
    Using Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
            
    return False
