# 207. Course Schedule

## 문제 요약
주어진 `numCourses`와 `prerequisites`를 통해 모든 코스를 수강할 수 있는지 여부를 판별하는 문제 (사이클이 존재하는지 확인).

## 사용한 개념
- **Topological Sort (위상 정렬)**: 칸 알고리즘(Kahn's Algorithm)을 사용하여 in-degree(진입 차수)가 0인 노드부터 순차적으로 탐색.
- **Graph (Adjacency List)**: `adj[pre] = [crs]` 형태로 그래프 구성.

## 복잡도
- 시간 복잡도: `O(V + E)` (모든 정점과 간선을 한 번씩 방문)
- 공간 복잡도: `O(V + E)` (인접 리스트와 in-degree 배열 저장)

## 오답 노트 및 엣지 케이스
- **엣지 케이스**: 
  - `prerequisites`가 비어있을 때: 무조건 `True`.
  - 그래프가 단절되어 있을 때(컴포넌트가 여러 개): in-degree가 0인 노드가 여러 개 들어가면서 자연스럽게 각각 처리됨.
- **주의점**:
  - `adj[pre].append(crs)`인지 `adj[crs].append(pre)`인지 방향 설정이 중요. 선행 과목(`pre`)을 들으면 들을 수 있는 과목(`crs`)으로 향하는 간선을 그려야 칸 알고리즘 적용 시 자연스러움.
  - 탐색 완료 후 `count == numCourses`로 체크하면 사이클 여부 확인이 한 번에 가능.
