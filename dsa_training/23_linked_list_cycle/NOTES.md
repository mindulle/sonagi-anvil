# Linked List Cycle Notes

## Edge Cases
- Empty List (`head is None`): Should return `False`.
- Single Node (`head.next is None`): Should return `False`.
- No Cycle: `fast` pointer reaches the end of the list.
- Cycle exists: `fast` and `slow` pointers meet inside the loop.

## Complexity
- Time: O(n) - Hare travels at most 2n steps.
- Space: O(1) - Uses only two pointers, regardless of list size.
