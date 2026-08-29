# Prompt
Implement Kadane's Algorithm to find the maximum subarray sum.
The algorithm should handle cases where all numbers are negative.

# Buggy Code
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum < 0:
                current_sum = 0
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
```

# Solution
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
```
