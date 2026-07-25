def coinChange(coins, amount):
    """
    주어진 동전 단위 배열 `coins`를 사용하여 목표 금액 `amount`를 만들 수 있는 최소 동전 개수를 구하세요.
    DP를 사용하여 해결하세요.
    """
    # TODO: Implement DP solution here
    if amount == 0:
        return 0
    if not coins:
        return -1

    # dp[i] will be the minimum coins needed for amount i
    # Initialize with amount + 1 (which is effectively infinity)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] <= amount else -1
