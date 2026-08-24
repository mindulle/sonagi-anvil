# 48. Rotate Image (Medium)

## 핵심 아이디어
- 2D 매트릭스를 제자리에서(in-place) 90도 시계방향으로 회전시키려면 다음과 같은 수학적 변환을 이용하면 매우 간단합니다.
1. **전치 (Transpose)**: `matrix[i][j]` 와 `matrix[j][i]` 를 스왑. (단, `j`는 `i`부터 `n`까지)
2. **좌우 반전 (Reverse each row)**: 각 행을 `reverse()` 시킴.

## 복잡도
- Time Complexity: $O(N^2)$ (모든 원소를 2번씩 방문)
- Space Complexity: $O(1)$ (in-place)

## 엣지 케이스 및 실수하기 쉬운 점
- 전치(Transpose) 시 안쪽 루프의 인덱스 `j`가 `i`부터 시작해야 합니다. `0`부터 시작하면 원위치로 다시 스왑되어 전치가 이루어지지 않습니다.
- 90도 반시계 방향(Counter-clockwise) 회전의 경우, '좌우 반전 후 전치' 하거나 '상하 반전 후 전치' 등으로 응용할 수 있습니다.
