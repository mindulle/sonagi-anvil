# Prompt
"정수 배열 `nums`와 정수 `target`이 주어집니다. 배열 안의 두 숫자를 더해서 `target`이 되는 두 숫자의 '인덱스'를 배열 형태로 반환하는 파이썬 함수를 만들어줘. 정답은 무조건 1개만 존재한다고 가정해."

# Buggy Code
```python
def two_sum(nums, target):
    # Iterate through each element in the array
    for i in range(len(nums)):
        for j in range(len(nums)):
            # Check if the sum equals the target
            if nums[i] + nums[j] == target:
                return [i, j]
```

# Solution
### 1. Logic Bug (치명적인 논리 오류)
**문제점:** 이 코드는 `i`와 `j`가 같은 값을 가질 수 있도록 허용합니다. 만약 `nums = [3, 2, 4]` 이고 `target = 6`이라면, 이 코드는 요소 3을 두 번 더해서 (3+3=6) `[0, 0]`을 반환하고 실패합니다.
**수정:** 내부 루프는 `for j in range(i + 1, len(nums)):` 로 변경되어야 합니다.

### 2. Complexity (시간 복잡도)
**현재:** 이중 for문을 사용하므로 **O(N²)** Time Complexity를 가집니다.
**최적화:** **Hash Map (Dictionary)**를 사용하여 한 번의 순회로 해결할 수 있습니다. `target - nums[i]` 값이 딕셔너리에 존재하는지 확인하면 **O(N)**으로 줄일 수 있습니다.

### 3. Ideal English Feedback
"The model's code fails due to a critical logic bug: it allows using the same element twice because the inner loop starts at 0 instead of `i + 1`. If `nums = [3, 2, 4]` and `target = 6`, it incorrectly returns `[0, 0]`.
Additionally, the solution is highly inefficient with an O(N²) time complexity. It should be optimized using a Hash Map to store previously seen values and their indices, which would reduce the time complexity to O(N)."
