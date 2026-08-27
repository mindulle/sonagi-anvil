# Anki Review 2026-07-30

## Algorithm: 30_longest_increasing_subsequence

### Concept
- Dynamic Programming for LIS (Longest Increasing Subsequence).
- Time Complexity: O(n^2) for the DP approach shown.
- Space Complexity: O(n) for the DP array.

### Key Insight
- `dp[i]` represents the LIS ending at index `i`.
- `dp[i] = max(dp[j] + 1)` for all `j < i` where `nums[j] < nums[i]`.
- Can it be optimized? Yes, to O(n log n) using binary search (patience sorting).

### Reflection
The O(n^2) DP is the classic approach and easier to implement, but O(n log n) is better for larger inputs. I should review the O(n log n) approach next time.
