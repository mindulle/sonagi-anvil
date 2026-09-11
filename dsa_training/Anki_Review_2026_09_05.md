# Anki Review - 2026-09-05

## 1. 57_missing_number
- **Concept:** XOR to find missing number
- **Review Note:** XOR property: `a ^ a = 0` and `a ^ 0 = a`. We can XOR all numbers in the array with all numbers from `0` to `n`. The remaining number is the missing one.
- **Rating:** Hard -> Good

## 2. 56_house_robber
- **Concept:** Dynamic Programming
- **Review Note:** Remember `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. Optimize space by keeping track of only the last two values instead of an entire array.
- **Rating:** Good -> Easy
