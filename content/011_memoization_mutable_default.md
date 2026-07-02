# Prompt
"피보나치 수열을 메모이제이션을 활용해 구현하세요."

# Buggy Code
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

# Solution
### 1. Python Specific Bug (Mutable Default Argument)
**문제점:** `memo={}` 와 같이 Mutable 객체를 기본 인자로 설정하면, 함수가 정의될 때 한 번만 인스턴스화됩니다. 따라서 여러 번 `fib()`를 독립적으로 호출할 때 이전 호출의 결과가 `memo`에 계속 남아있게 되어 예상치 못한 부작용이나 메모리 릭이 발생할 수 있습니다.
**수정:** `memo=None`으로 설정하고, 함수 내부에서 `if memo is None: memo = {}`로 초기화해야 합니다.
