# Kth Largest Element in an Array

# Prompt
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.
Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.
You must solve it in `O(n)` time complexity if possible, or `O(n log k)` using a heap.

# Buggy Code
```python
def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]
```
(Sorting takes O(N log N) which is suboptimal compared to the heap approach of O(N log k)).

# Solution
Use a min-heap of size `k`. As we iterate through the numbers, we push to the heap. If the size of the heap exceeds `k`, we pop the smallest element. At the end, the top of the heap will be the `k`th largest element.

```python
import heapq
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    """
    Time Complexity: O(N log k)
    Space Complexity: O(k)
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
```

Feedback: "When dealing with finding the 'Kth largest/smallest', always consider a Heap of size K as it optimizes the sorting step from O(N log N) to O(N log K)."
