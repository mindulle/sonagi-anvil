# Prompt
"두 개의 정렬된 정수 배열 `nums1`과 `nums2`가 주어집니다. `nums1`의 크기는 `m+n`이고 `nums2`의 크기는 `n`입니다. `nums1`과 `nums2`를 합쳐서 `nums1` 하나로 정렬된 상태로 만들어줘. 추가 배열을 생성하지 말고 `nums1`을 직접 수정(in-place)해야 해."

# Buggy Code
```python
def merge(nums1, m, nums2, n):
    # 단순히 nums2를 nums1 뒤에 붙이고 정렬하는 방식
    for i in range(n):
        nums1[m + i] = nums2[i]
    nums1.sort()
```

# Solution
### 1. Complexity (시간 복잡도)
**현재:** `nums1.sort()`를 사용하므로 **O((M+N)log(M+N))** Time Complexity를 가집니다.
**최적화:** 두 배열이 이미 정렬되어 있다는 점을 활용하여 뒤에서부터 채워 넣는 3-pointer 방식을 사용하면 **O(M+N)** Time Complexity로 해결할 수 있습니다.

### 2. Implementation (구현 방법)
1. `nums1`의 마지막 유효 요소(`p1 = m - 1`)와 `nums2`의 마지막 요소(`p2 = n - 1`)를 가리키는 포인터를 만듭니다.
2. `nums1`의 마지막 위치(`p = m + n - 1`)부터 두 포인터가 가리키는 값을 비교하여 더 큰 값을 채워 넣습니다.

### 3. Ideal English Feedback
"The current solution uses `nums1.sort()`, which is inefficient with a time complexity of O((M+N)log(M+N)). Since both arrays are already sorted, you can achieve O(M+N) time complexity by using a three-pointer approach. Start filling `nums1` from the end (index `m+n-1`) by comparing elements from the end of `nums1` and `nums2` and moving backwards. This avoids unnecessary sorting and extra space."
