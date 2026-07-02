# ⚔️ Sonagi Anvil: DSA 실기 훈련장

이 디렉토리(`dsa_training/`)는 Dataannotation, Outlier, Alignerr 등 AI 코드 리뷰어/데이터 라벨링 플랫폼의 **코딩 어세스먼트(Assessment)**를 통과하기 위한 TDD(Test-Driven Development) 기반 반복 훈련장입니다.

## 🚀 훈련 시나리오 (How to Train)

이 훈련장의 핵심은 **'백지 상태에서 테스트 코드를 통과할 때까지 반복해서 코딩하는 것(Coding Kata)'**입니다.

### 1. 훈련 초기화 (리셋)
훈련을 시작하기 전, 프로젝트 루트 디렉토리에서 아래 스크립트를 실행하면 모든 문제 코드가 `TODO`가 작성된 초기 빈 깡통 상태로 리셋됩니다.
*(주의: 작성하던 코드는 모두 날아가므로, 보존해야 하는 해결 코드는 반드시 GitHub PR을 통해 `main`에 병합하거나 별도 브랜치로 커밋해 두세요!)*

```bash
cd sonagi-anvil
./reset_training.sh
```

### 2. TDD 기반 문제 풀이
초기화가 끝나면, 풀고자 하는 문제 폴더(예: `02_valid_parentheses/`)로 이동하여 파이썬 파일을 엽니다.
테스트 파일(`test_*.py`)은 **절대 수정하지 않고**, 로직 파일(`*.py`)의 `TODO` 영역에 코드를 작성합니다.

코드를 작성하면서 로컬 터미널에 다음을 반복적으로 실행하며 테스트를 100% 통과(Pass)시키세요.
```bash
cd dsa_training
pytest
```
* 특정 문제만 테스트하고 싶을 땐 `pytest 02_valid_parentheses/test_valid_parentheses.py` 처럼 실행합니다.

### 3. 모의 면접 (블라인드 엣지 케이스 분석)
로컬에서 100% 초록 불(Pass)을 보았다면, 본인이 작성한 코드를 보며 다음을 스스로 검증해보세요. (어세스먼트 리뷰어 역할)
- "이 코드의 시간/공간 복잡도(Big-O)는 최적인가?"
- "입력값이 빈 배열 `[]`이거나 `None`일 때 터지지 않는가?"
- "가장 극단적인 크기의 값이 들어올 때 오버플로우나 `RecursionError`가 나진 않는가?" 

### 4. 새로운 문제 추가
어세스먼트 대비를 위해 새로운 문제를 훈련장에 추가하려면 다음 규칙을 따르세요:
1. `dsa_training/` 하위에 문제 폴더 생성 (예: `05_merge_intervals`)
2. `merge_intervals.py` (빈 뼈대 코드 + TODO 작성) 생성
3. `test_merge_intervals.py` (엣지 케이스를 모두 포함한 pytest 검증 코드) 생성
4. **[중요]** 이후에도 계속 반복 훈련을 하기 위해, 완성된 빈 뼈대 코드를 `dsa_training/.templates/05_merge_intervals/` 로 복사해 두십시오. (`reset_training.sh`가 이를 바탕으로 복구합니다.)

---

## 🛠️ 자주 틀리는 알고리즘 체크리스트 (Anki용)
이 훈련장에서 반복하며 깨달은 본인의 약점은 반드시 `anki.sonagi.space` 에 플래시카드로 등록하세요.
* `Number of Islands` → 큰 그리드에서는 재귀(Recursive DFS) 시 RecursionError 발생 위험! Stack을 쓴 Iterative DFS 사용.
* `LRU Cache` → 직접 Doubly Linked List + Hash Map을 짜는 것보다, 실무와 파이썬 코테에서는 `collections.OrderedDict` (`move_to_end`, `popitem`)이 압도적으로 유리함.

## 🚨 엣지 케이스(Edge Case) 치트시트 (유형별 암기법)
어세스먼트나 코딩 인터뷰에서 코드 리뷰를 할 때, 코드를 한 줄씩 읽기 전에 **'입력 데이터의 유형'**만 보고 반사적으로 떠올려야 하는 엣지 케이스 패턴입니다. 이 치트시트를 통째로 Anki에 넣고 외우면 리뷰 속도와 정확도가 비약적으로 상승합니다.

| 데이터 타입 | 반사적으로 테스트해봐야 할 엣지 케이스 (입력값) | 발생하기 쉬운 버그 / 에러 |
| :--- | :--- | :--- |
| **Array / String** | 빈 배열/문자열 (`[]`, `""`), Null (`None`) | `IndexError`, `NullPointerException` |
| | 원소가 딱 1개일 때 (`[a]`, `"x"`) | 투 포인터 엇갈림, 루프 미실행 |
| | 모든 원소가 동일할 때 (`[2,2,2,2]`, `"aaaa"`) | 무한 루프, Set 중복 제거로 인한 로직 파괴 |
| | 이미 정렬됨 / 역순 정렬됨 (`[1,2,3]`, `[3,2,1]`) | QuickSort의 $O(n^2)$ 최악의 시간 복잡도 발생 |
| **Integer / Math** | `0`, 음수 (`-1`) | `ZeroDivisionError`, 인덱스 뒤로가기 버그 |
| | 시스템 최대/최소값 (`sys.maxsize`, `-sys.maxsize`) | `OverflowError` (파이썬 외 언어에서 특히 중요) |
| **Graph / Tree** | 노드가 1개이거나 아예 없는(Root=None) 경우 | 초기화 에러, 무한 재귀 |
| | 트리가 한쪽으로만 치우친 경우 (Linked List 형태) | 재귀 깊이 초과 (`RecursionError`) |
| | 사이클(Cycle)이 존재하는 그래프 (A->B->C->A) | 무한 루프 (방문 처리 `visited` 누락 시) |
| **기타 (동시성 등)**| 동일한 자원에 동시 접근 / 빈번한 I/O | `Race Condition`, 병목 현상, 데드락 |
