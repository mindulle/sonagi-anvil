import pytest
from rate_limiter import RateLimiter

class MockRedis:
    def __init__(self):
        self.data = {}
        self.expiry = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value, ex=None):
        self.data[key] = value
        self.expiry[key] = ex

    def incr(self, key):
        self.data[key] = self.data.get(key, 0) + 1
        return self.data[key]

def test_rate_limiter():
    redis = MockRedis()
    limiter = RateLimiter(redis)
    user_id = "user1"
    
    # 100 requests should be allowed
    for _ in range(100):
        assert limiter.is_allowed(user_id) is True
    
    # 101st should be denied
    assert limiter.is_allowed(user_id) is False
