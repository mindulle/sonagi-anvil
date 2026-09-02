# Prompt
Find the minimum number of coins that make up the given amount.
A greedy approach may not work, so use Dynamic Programming.

# Buggy Code
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        count = 0
        for coin in coins:
            count += amount // coin
            amount %= coin
        return count if amount == 0 else -1
```

# Solution
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```
