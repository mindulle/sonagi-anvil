# Prompt
Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

# Buggy Code
```python
def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path) # Bug: appends a reference to path, not a copy
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res
```

# Solution
When appending a mutable object (like a list) to another list in Python, you must append a copy (`path[:]` or `list(path)`), otherwise all references will point to the same modified list, leading to incorrect results (usually a list of empty lists at the end).

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    def backtrack(start, path):
        # Append a copy of path
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res
```

**Complexity Analysis**
- Time Complexity: O(N * 2^N) where N is the number of elements. We generate 2^N subsets, and for each subset, it takes O(N) to copy it to the result array.
- Space Complexity: O(N) auxiliary space for the recursion stack and `path` array (not counting the output list which takes O(N * 2^N)).
