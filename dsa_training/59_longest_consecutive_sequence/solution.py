def longest_consecutive(nums: list[int]) -> int:
    """
    Time Complexity: O(n) where n is the length of nums.
    Space Complexity: O(n) for the hash set.
    """
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak
