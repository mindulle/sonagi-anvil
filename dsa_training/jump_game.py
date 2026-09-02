def can_jump(nums: list[int]) -> bool:
    """
    Jump Game
    Time Complexity: O(N) where N is the length of nums
    Space Complexity: O(1)
    """
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
        if max_reach >= len(nums) - 1:
            return True
    return True
