def letter_combinations(digits: str) -> list[str]:
    """
    Time Complexity: O(4^N * N) where N is the length of digits.
    Space Complexity: O(N) for the recursion stack.
    """
    if not digits:
        return []
        
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    res = []
    
    def backtrack(i: int, cur_str: str):
        if len(cur_str) == len(digits):
            res.append(cur_str)
            return
            
        for c in phone_map[digits[i]]:
            backtrack(i + 1, cur_str + c)
            
    backtrack(0, "")
    return res
