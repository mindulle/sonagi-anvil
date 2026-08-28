from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    
    Time Complexity: O(N * 2^N) - generating all subsets and copying them.
    Space Complexity: O(N * 2^N) - storing all subsets, or O(N) auxiliary stack space for recursion.
    """
    res = []
    
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
    backtrack(0, [])
    return res
