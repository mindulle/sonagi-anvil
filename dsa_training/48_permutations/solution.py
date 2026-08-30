from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(N * N!), where N is the length of nums.
                         There are N! permutations and we take O(N) to copy each permutation.
        Space Complexity: O(N), for the recursion stack and the current path.
        """
        res = []
        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    path.append(num)
                    dfs(path, used)
                    path.pop()
                    used[i] = False
                    
        dfs([], [False] * len(nums))
        return res
