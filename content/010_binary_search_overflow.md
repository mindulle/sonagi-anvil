# Prompt
"정렬된 배열에서 이진 탐색(Binary Search)을 구현하세요."

# Buggy Code
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

# Solution
### 1. Potential Overflow (Integer Overflow)
**문제점:** 파이썬은 임의 정밀도 정수를 지원하므로 이 코드는 파이썬에서는 안전하지만, 일반적인 C/C++/Java 인터뷰 관점에서는 `mid = (left + right) // 2`가 오버플로우를 유발할 수 있는 잠재적 결함입니다.
**수정:** `mid = left + (right - left) // 2` 로 작성하는 것이 언어에 무관하게 안전한 모범 답안입니다.
