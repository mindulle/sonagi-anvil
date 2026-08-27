from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums. You are initially positioned at the array's first index, 
        and each element in the array represents your maximum jump length at that position.
        Return true if you can reach the last index, or false otherwise.
        
        Time Complexity: O(n) - We traverse the array once.
        Space Complexity: O(1) - We only store the max_reachable index.
        """
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
            if max_reachable >= len(nums) - 1:
                return True
        return False
