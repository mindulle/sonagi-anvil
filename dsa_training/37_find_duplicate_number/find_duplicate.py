def findDuplicate(nums):
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.
    """
    # Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
    slow = nums[0]
    fast = nums[0]
    
    # Phase 1: Finding the intersection point in the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # Phase 2: Finding the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow
