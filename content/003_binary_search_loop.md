# Prompt
"정렬된 정수 배열 `nums`와 찾고자 하는 값 `target`이 주어집니다. `target`이 배열에 존재하면 해당 인덱스를, 없으면 -1을 반환하는 Binary Search (이진 탐색) 함수를 작성해줘."

# Buggy Code
```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
            
    return -1
```

# Solution
### 1. Logic Bug / Edge Case
**문제점:** 치명적인 **무한 루프(Infinite Loop)** 버그가 있습니다. `target`을 찾지 못해 범위를 좁혀야 할 때, `left = mid` 또는 `right = mid`로 업데이트하면 범위가 1 이하로 좁혀졌을 때 `mid`가 계속 제자리에 머물게 됩니다. (예: `left=0`, `right=1` 일 때 `mid=0`이 반복됨)
**수정:** `left = mid + 1`, `right = mid - 1` 로 변경하여 탐색한 `mid`를 다음 범위에서 완전히 제외해야 합니다.

### 2. Complexity & Optimization
**현재:** `while` 문 로직 수정 후에는 시간 복잡도 **O(log N)**, 공간 복잡도 **O(1)** 로 최적의 상태입니다. (단, Python 외 언어에서는 `mid = left + (right - left) // 2` 를 사용하여 Integer Overflow를 방지해야 하지만 파이썬은 자동으로 큰 정수를 지원하므로 생략 가능합니다.)

### 3. Ideal English Feedback
"The generated code contains a critical logic error that results in an infinite loop. Inside the `while` loop, you update the pointers as `left = mid` and `right = mid`. When the search space narrows down to two adjacent elements, `mid` will repeatedly evaluate to `left`, causing the loop to never terminate.

To fix this, you must exclude the already checked `mid` element from the next search space. Update the pointers to `left = mid + 1` and `right = mid - 1` respectively."
