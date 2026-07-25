class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, determine if it is a palindrome, considering only
        alphanumeric characters and ignoring cases.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
