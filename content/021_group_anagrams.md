# Prompt
"문자열 배열을 입력받아 애너그램(Anagram) 그룹을 묶으세요."

# Buggy Code
```python
def groupAnagrams(strs):
    result = []
    for s in strs:
        # Naive approach: check if s is an anagram of any group
        found = False
        for group in result:
            if sorted(s) == sorted(group[0]):
                group.append(s)
                found = True
                break
        if not found:
            result.append([s])
    return result
```

# Solution
### 1. Character Count Optimization
**문제점:** 문자열을 매번 정렬하는 것은 KlogK 복잡도를 가집니다.
**수정:** 문자열을 정렬하는 대신, 각 문자의 빈도수(Character Count)를 튜플이나 문자열로 변환하여 해시맵의 키로 사용하면 O(N * K) 복잡도로 최적화할 수 있습니다.

### 2. Handling Special Characters
**수정:** 입력 문자열에 공백이나 특수 문자가 포함될 경우에 대한 처리도 함께 고려되어야 합니다.
