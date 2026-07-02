# Prompt
"Redis를 사용하는 간단한 API Rate Limiter를 작성해주세요. 사용자 ID당 분당 100회로 제한합니다."

# Buggy Code
```python
def is_allowed(user_id, redis_client):
    key = f"rate_limit:{user_id}"
    requests = redis_client.get(key)
    if requests is None:
        redis_client.set(key, 1, ex=60)
        return True
    if int(requests) >= 100:
        return False
    redis_client.incr(key)
    return True
```

# Solution
### 1. Race Condition (동시성 오류)
**문제점:** `.get()` 과 `.incr()` 사이에 원자성(Atomicity)이 보장되지 않습니다. 두 스레드가 동시에 `get`을 호출하여 99를 읽으면 둘 다 `incr`을 실행해 실제로는 101번의 요청이 허용될 수 있습니다.
**수정:** Redis의 `INCR` 명령어를 먼저 사용하고, 반환값이 1일 때 `EXPIRE`를 설정하는 방식이 원자적이며 안전합니다. 또는 Lua 스크립트를 사용해야 합니다.
