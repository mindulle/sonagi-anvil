# Prompt
Given an array `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Return the max sliding window.

# Buggy Code
```python
def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        res.append(max(nums[i:i+k]))
    return res
```

# Solution
### 1. Logic Bug (성능 오류)
**문제점:** 이 코드는 논리적으로는 맞지만, 매 윈도우마다 `max()` 함수를 호출하여 O(N*k)의 시간 복잡도를 가집니다. k가 클 경우 매우 비효율적입니다.
**수정:** Monotonic Deque(단조 큐)를 사용하여 각 요소를 한 번씩만 추가/제거함으로써 **O(N)** 시간 복잡도로 최적화해야 합니다.

### 2. Complexity (시간 복잡도)
**현재:** O(N*k) - 윈도우마다 `max()` 수행.
**최적화:** O(N) - Monotonic Deque 사용.

### 3. Ideal English Feedback
"The model's implementation uses a naive O(N*k) approach by calling `max()` on each window. While functionally correct, this is highly inefficient for large values of `k`.
The optimal solution should utilize a monotonic deque to maintain indices of elements in the current window in decreasing order. This allows finding the maximum in constant time, reducing the overall time complexity to O(N)."
