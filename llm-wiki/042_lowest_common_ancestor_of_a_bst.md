# 42. Lowest Common Ancestor of a Binary Search Tree

## 놓친 조건 / 엣지 케이스
- BST(Binary Search Tree)의 특성을 활용하면 전체 트리를 탐색할 필요가 없음.
- 현재 노드의 값이 `p`와 `q`의 값보다 모두 크면, LCA는 무조건 왼쪽 서브트리에 있음.
- 반대로 모두 작으면, LCA는 무조건 오른쪽 서브트리에 있음.
- 그 외의 경우(하나보다 크고 다른 하나보다 작거나 같은 경우), 현재 노드가 갈라지는 지점(split point)이므로 이 노드가 바로 LCA가 됨.

## 패턴 메모
- 일반 이진 트리(Binary Tree)의 LCA는 Bottom-Up (재귀) 탐색이 필요하지만, BST의 경우 Top-Down (반복문)으로 O(1) 공간 복잡도로 해결 가능.
- `while current:` 구조 내에서 분기를 타서 내려가는 방식이 매우 깔끔함.
