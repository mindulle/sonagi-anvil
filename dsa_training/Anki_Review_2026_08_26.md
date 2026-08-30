# Anki Review - 2026-08-26

## 1. 알고리즘: Letter Combinations of a Phone Number
- **패턴**: Backtracking (백트래킹)
- **Time Complexity**: $O(4^N \times N)$
  - 4 is the maximum number of letters mapped to a digit (e.g., '7', '9').
  - N is the number of digits. The height of the recursion tree is N.
  - Adding the string to the result takes O(N) time.
- **Space Complexity**: $O(N)$ for the recursion call stack.
- **엣지 케이스**: `digits`가 빈 문자열일 때 `[""]`가 아니라 `[]`를 리턴해야 함을 주의할 것.
- **리뷰**: 기본 백트래킹 뼈대(base case: `len(cur_str) == len(digits)`)를 명확히 세우면 쉽게 풀 수 있는 문제.

## 2. Anki 복습 완료
- 어제 정리한 Subsets 문제 백트래킹 템플릿 복습 완료
