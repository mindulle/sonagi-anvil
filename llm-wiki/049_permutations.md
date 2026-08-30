# LeetCode 46. Permutations

## 오답 노트 및 엣지 케이스 (Edge Cases & Mistakes)
- **Edge Case**: `nums` 배열의 길이가 1인 경우. (이 경우에도 올바르게 1개의 요소를 가진 리스트를 반환해야 함)
- **실수하기 쉬운 부분**: 
  - Python에서 `res.append(path)`를 하면 참조가 들어가기 때문에 이후에 `path`를 변경하면 `res` 안의 배열도 변경됨. 반드시 `res.append(path[:])` 또는 `res.append(list(path))`로 깊은 복사(shallow copy)를 해서 넣어야 함.
  - 시간 복잡도는 순열의 개수인 N!번 복사(N)가 일어나므로 O(N * N!)가 됨.

## 팁 (Tips)
- Backtracking을 구현할 때 상태 배열(`used`)을 사용하면 각 원소의 포함 여부를 빠르게 O(1)로 체크할 수 있다.
- DFS 종료 조건은 `len(path) == len(nums)` 일 때.
