# Prompt

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

# Buggy Code

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
```

# Solution

The buggy code fails to check if the bounds are still valid before iterating over the bottom row and the left column. Since `top` and `right` are updated in the middle of the loop, we must check if `left <= right` and `top <= bottom` again to prevent duplicate printing in cases like a 1D matrix or when the remaining inner matrix is a single row or column.

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
            
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            # get every i in the top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # get every i in the right col
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if not (left <= right and top <= bottom):
                break
                
            # get every i in the bottom row
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
            # get every i in the left col
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
```

**Time Complexity**: `O(m * n)` where `m` is the number of rows and `n` is the number of columns. We visit each element of the matrix exactly once.
**Space Complexity**: `O(1)` (excluding the output array `res`) since we only maintain boundary pointers.
