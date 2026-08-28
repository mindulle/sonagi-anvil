# Anki Review 2026-08-06

## Algorithm Practice
- **Problem**: 37. Find the Duplicate Number (LeetCode 287)
- **Key Concepts**: Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
- **Notes**:
    - The problem asks for the duplicate number in an array of size n+1 with numbers in [1, n].
    - Since we cannot modify the array, sorting is not allowed (O(n log n)).
    - Since we need O(1) space, hash set is not allowed (O(n)).
    - Floyd's Cycle-Finding Algorithm treats the array as a linked list where `index -> value` is a pointer.
    - Because there's a duplicate, there *must* be a cycle.
    - Time complexity: O(n), Space complexity: O(1).

## Anki Cards to Add
1. Q: How to detect a duplicate number in an array of [1, n] using O(1) space and O(n) time?
   A: Treat the array as a linked list where `nums[i]` is the next pointer. Since there's a duplicate, the "linked list" has a cycle. Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare) to detect the entrance to the cycle, which is the duplicate number.
