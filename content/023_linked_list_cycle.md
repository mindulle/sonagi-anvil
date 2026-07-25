# Prompt
"Given head, the head of a linked list, determine if the linked list has a cycle in it. Aim for O(1) space."

# Buggy Code
```python
def hasCycle(head: ListNode) -> bool:
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False
```

# Solution
### 1. Space Complexity
**문제점:** 해시셋(`visited`)을 사용하여 방문한 노드를 저장하면 노드의 개수만큼 메모리가 사용되므로 공간 복잡도가 $O(n)$이 됩니다.
**수정:** **Floyd's Cycle-Finding Algorithm (Tortoise and Hare)**을 사용합니다.
- `slow` 포인터와 `fast` 포인터를 둡니다.
- `slow`는 한 칸씩, `fast`는 두 칸씩 이동합니다.
- 사이클이 있다면 `fast`가 `slow`를 따라잡게 됩니다.
이 방식은 추가적인 자료구조를 사용하지 않아 공간 복잡도가 $O(1)$입니다.
