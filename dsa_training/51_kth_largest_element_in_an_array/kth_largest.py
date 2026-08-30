import heapq
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    """
    Finds the kth largest element in an array.
    Time Complexity: O(N log k) where N is the length of nums.
    Space Complexity: O(k) for the min-heap.
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
