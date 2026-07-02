# Prompt
"주어진 동전 단위 배열 `coins`를 사용하여 목표 금액 `amount`를 만들 수 있는 최소 동전 개수를 구하세요."

# Buggy Code
```python
def coinChange(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count if amount == 0 else -1
```

# Solution
### 1. Logic Bug (Greedy Fallacy)
**문제점:** 모델은 그리디(Greedy) 접근법을 사용했습니다. 큰 동전부터 최대한 많이 사용하는 방식입니다. 그러나 동전 시스템이 배수 관계가 아닐 경우(예: `coins = [1, 3, 4]`, `amount = 6`) 오답을 반환합니다. 그리디는 4를 하나 고르고 1을 두 개 골라 총 3개를 반환하지만, 실제 정답은 3을 두 개 고르는 2개입니다.
**수정:** DP (Dynamic Programming) 또는 BFS 최단 거리 탐색 방식으로 해결해야 합니다.
