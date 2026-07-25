class RateLimiter:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def is_allowed(self, user_id):
        key = f"rate_limit:{user_id}"
        
        # Atomically increment and get value
        count = self.redis_client.incr(key)
        
        if count == 1:
            # Set expiry on first request
            self.redis_client.set(key, 1, ex=60)
        
        return count <= 100
