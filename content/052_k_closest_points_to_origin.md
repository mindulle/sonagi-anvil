# Prompt
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
You may return the answer in any order.

# Buggy Code
```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]
```

# Solution
- Using a max-heap of size `k` is optimal.
- When pushing to a max-heap in Python (which has a min-heap implementation by default), negate the distance.
- `heapq.heappush(max_heap, (-dist, x, y))`
- If the length of the heap exceeds `k`, pop the largest element out.
- The time complexity using a heap is O(N log k) whereas sorting all points is O(N log N).

Edge Cases:
- Duplicated distances.
- K equals the total number of points.
