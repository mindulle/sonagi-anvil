# Prompt
Appends a value to a list. If no list is provided, it should create a new one.
However, the current implementation has a bug related to mutable default arguments.
Fix the implementation.

# Buggy Code
```python
class Solution:
    def append_to_list(self, val, lst=[]):
        lst.append(val)
        return lst
```

# Solution
```python
class Solution:
    def append_to_list(self, val, lst=None):
        if lst is None:
            lst = []
        lst.append(val)
        return lst
```
