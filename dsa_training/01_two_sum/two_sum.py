from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        
        Time Complexity: O(n) - We traverse the list containing n elements only once.
        Space Complexity: O(n) - The extra space required depends on the number of items stored in the hash table, which stores at most n elements.
        """
        if not nums:
            return []
            
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
