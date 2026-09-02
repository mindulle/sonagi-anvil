\n## 2026-08-30: Spiral Matrix Pattern\n- When doing boundary-shrinking traversals (like spiral matrix), always remember to check if boundaries have crossed `left <= right and top <= bottom` after updating boundaries midway through the loop to avoid redundant reads.

## 2026-08-31: Jump Game Pattern
- Instead of checking all paths (backtracking), track the maximum reachable index (`max_reach = max(max_reach, i + jump)`). If the current index `i > max_reach`, it's impossible to proceed further. This greedy approach optimizes O(N^2) to O(N) time with O(1) space.

### Word Break (DP)
- DP array length should be `len(s) + 1`. 
- Base case `dp[0] = True` because empty string trivially forms valid words.
- Inner loop checks substring `s[j:i]`, if valid, set `dp[i] = True` and `break`.
