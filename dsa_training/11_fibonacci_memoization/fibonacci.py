class Solution:
    def fib(self, n: int, memo: dict = None) -> int:
        """
        피보나치 수열을 메모이제이션을 활용해 구현하세요.
        """
        if memo is None:
            memo = {}
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        return memo[n]
