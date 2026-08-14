from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity: O(N^(T/M)) where N is the number of candidates, 
        T is the target value, and M is the minimal value among the candidates.
        Space Complexity: O(T/M) for the recursion stack.
        """
        res = []
        
        def dfs(i, current_combo, total):
            if total == target:
                res.append(current_combo.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # Include candidates[i]
            current_combo.append(candidates[i])
            dfs(i, current_combo, total + candidates[i])
            current_combo.pop()
            
            # Skip candidates[i]
            dfs(i + 1, current_combo, total)
            
        dfs(0, [], 0)
        return res
