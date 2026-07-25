from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array to the right by k steps, 
        where k is non-negative.
        
        Do not return anything, modify nums in-place instead.
        
        Time Complexity: O(n)
        Space Complexity: O(1) (if using reversal approach) or O(n) (if using slicing)
        """
        if not nums:
            return
        
        n = len(nums)
        k %= n
        
        # Using slicing (O(n) space)
        nums[:] = nums[n-k:] + nums[:n-k]
