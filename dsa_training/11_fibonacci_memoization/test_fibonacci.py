import pytest
from fibonacci import Solution

def test_fibonacci():
    sol = Solution()
    assert sol.fib(0) == 0
    assert sol.fib(1) == 1
    assert sol.fib(2) == 1
    assert sol.fib(3) == 2
    assert sol.fib(10) == 55
