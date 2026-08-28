from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        TODO: Implement Kadane's algorithm to find the maximum subarray sum.
        Ensure it handles an array with ONLY negative numbers correctly.
        """
        if not nums:
            return 0
        
        max_so_far = nums[0]
        current_max = nums[0]
        
        for x in nums[1:]:
            current_max = max(x, current_max + x)
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far
