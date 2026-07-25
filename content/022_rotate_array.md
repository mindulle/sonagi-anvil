# Prompt
"Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. Do not return anything, modify nums in-place instead. Aim for O(1) extra space."

# Buggy Code
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        # Using slicing creates a new array of size n, which is O(n) space
        nums[:] = nums[n-k:] + nums[:n-k]
```

# Solution
### 1. Space Complexity
**문제점:** 슬라이싱(`nums[n-k:] + nums[:n-k]`)은 새로운 배열을 생성하므로 $O(n)$ 공간을 사용합니다. 문제의 의도가 $O(1)$ 추가 공간 사용이라면 이 방식은 개선이 필요합니다.
**수정:** **Reversal Approach(역순 알고리즘)**를 사용합니다.
1. 전체 배열을 뒤집습니다.
2. 처음 k개 요소를 뒤집습니다.
3. 나머지 n-k개 요소를 뒤집습니다.
이 방식은 추가 공간 없이 $O(1)$ 공간 복잡도로 해결할 수 있습니다.
