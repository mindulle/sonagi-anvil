class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Given an array nums, there is a sliding window of size k which is moving from the very left 
        of the array to the very right. You can only see the k numbers in the window. 
        Return the max sliding window.
        """
        from collections import deque
        
        result = []
        d = deque()  # stores indices
        for i, n in enumerate(nums):
            # Remove indices that are out of the window
            if d and d[0] <= i - k:
                d.popleft()
            
            # Remove indices whose corresponding values are less than the current value
            while d and nums[d[-1]] < n:
                d.pop()
            
            d.append(i)
            
            # If window is full, add the max to result
            if i >= k - 1:
                result.append(nums[d[0]])
                
        return result
