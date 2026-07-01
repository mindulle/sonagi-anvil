# Prompt
Implement an LRU (Least Recently Used) cache. The cache should be initialized with a positive `capacity`.
`get(key)`: Return the value of the key if the key exists, otherwise return -1.
`put(key, value)`: Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions `get` and `put` must each run in O(1) average time complexity.

# Buggy Code
```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.usage_history = []

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update history: remove key and append to the end
            self.usage_history.remove(key)
            self.usage_history.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.usage_history.remove(key)
            self.usage_history.append(key)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used key
                lru_key = self.usage_history.pop(0)
                del self.cache[lru_key]
            
            self.cache[key] = value
            self.usage_history.append(key)
```

# Solution
## Flaw Identification
The generated code implements the LRU Cache using a dictionary `self.cache` and a Python list `self.usage_history`. While functionally correct for maintaining the LRU order, it heavily violates the O(1) time complexity requirement specified in the prompt.

1. **O(N) Time Complexity in `remove`**: Python's list `remove(key)` method runs in O(N) time because it has to scan the list to find the element and then shift all subsequent elements. This happens in both `get` and `put`.
2. **O(N) Time Complexity in `pop(0)`**: Removing the first element of a list using `pop(0)` also takes O(N) time because it requires shifting all remaining elements to the left.

## Suggested Fix
To achieve O(1) time complexity for both operations, the cache must be implemented using a combination of a Hash Map and a Doubly Linked List. Alternatively, in Python 3.7+, `collections.OrderedDict` can be used as it is implemented via a doubly linked list under the hood and preserves insertion order natively in O(1) time.

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed item to the end to mark it as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and mark as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # Evict if capacity exceeded
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) # popitem(last=False) pops in FIFO order
```
