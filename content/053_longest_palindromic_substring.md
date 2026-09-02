# Prompt
Given a string `s`, return the longest palindromic substring in `s`.

# Buggy Code
```python
def longest_palindrome(s: str) -> str:
    # A common brute-force approach that causes Time Limit Exceeded (TLE)
    res = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub) > len(res):
                res = sub
    return res
```

# Solution
```python
def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    
    start, end = 0, 0
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand_around_center(i, i)       
        len2 = expand_around_center(i, i + 1)   
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]
```
The brute-force solution is O(N^3) time complexity and will fail on large inputs. By using the "Expand Around Center" technique, we treat each character (and each pair of characters) as a potential center of a palindrome, expanding outwards. This reduces the time complexity to O(N^2) and maintains O(1) space complexity.
