from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search implementation that is safe from potential integer overflow
        in languages with fixed-size integer types by using the formula
        mid = left + (right - left) // 2 instead of mid = (left + right) // 2.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            # Use left + (right - left) // 2 for overflow safety
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
