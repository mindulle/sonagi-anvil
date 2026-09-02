# Anki Review 2026-07-31

## Algorithm Practice
- **Problem**: 33. Merge K Sorted Lists
- **Key Concepts**: Min-Heap (Priority Queue), Linked List
- **Notes**: 
    - Use a min-heap to always pick the smallest element among the current head nodes of the K lists.
    - Time Complexity: O(N log K), where N is total nodes, K is number of lists.
    - Space Complexity: O(K) for the heap.

## Anki Cards to Add (Mental Check)
1. Q: How to efficiently merge K sorted linked lists?
   A: Use a min-heap to store the head of each list. Continuously extract the minimum and push the next node from that list into the heap. O(N log K) time.
