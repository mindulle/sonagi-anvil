def rob(nums: list[int]) -> int:
    """
    Time Complexity: O(N) where N is the length of nums. We iterate through the array once.
    Space Complexity: O(1) as we only use two variables to keep track of the max loot.
    """
    if not nums:
        return 0
        
    rob1, rob2 = 0, 0
    
    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
        
    return rob2
