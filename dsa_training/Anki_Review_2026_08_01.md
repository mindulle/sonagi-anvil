# Anki Review 2026-08-01

## Algorithm Practice
- **Problem**: 34. Search in Rotated Sorted Array
- **Key Concepts**: Binary Search on Rotated Array
- **Notes**: 
    - The key observation is that in a rotated sorted array, at least one half (left or right) is always sorted.
    - Compare `nums[mid]` with `nums[left]` or `nums[right]` to determine which half is sorted, then check if target lies within that sorted range.
    - Time Complexity: O(log N).
    - Space Complexity: O(1).

## Anki Cards to Add (Mental Check)
1. Q: How to binary search in a rotated sorted array?
   A: After computing `mid`, identify which half is sorted by comparing `nums[mid]` with `nums[left]`. If left is sorted (`nums[left] <= nums[mid]`), check if `target` is in `[nums[left], nums[mid])`. Else, check the right half.
