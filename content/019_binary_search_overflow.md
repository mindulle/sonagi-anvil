# Prompt
"이진 탐색(Binary Search) 알고리즘을 구현하세요. 정렬된 배열에서 타겟 값을 찾으면 인덱스를 반환하고, 없으면 -1을 반환합니다."

# Buggy Code
(모델의 답변 요약)
"```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```"

# Solution
### 1. Integer Overflow
**문제점:** `mid = (low + high) // 2` 는 `low + high`가 매우 클 경우 정수 오버플로우가 발생할 수 있습니다 (언어에 따라).
**수정:** `mid = low + (high - low) // 2` 로 변경하여 오버플로우를 예방해야 합니다.
