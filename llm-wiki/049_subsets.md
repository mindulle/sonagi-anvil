# 049_subsets

## Pattern: Backtracking
- Subsets (Power Set) generation.
- **Key Takeaway**: Use backtracking to explore all combinations.
- **Common Trap**: Appending a reference to `path` (`res.append(path)`) instead of a copy (`res.append(path[:])`). This leads to the result containing multiple references to the same modified list, ending with all empty lists.
- **Edge Cases**: Empty list (`[]` -> `[[]]`), single element (`[0]` -> `[[], [0]]`).

## Complexity
- Time: O(N * 2^N)
- Space: O(N) auxiliary space (excluding result).
