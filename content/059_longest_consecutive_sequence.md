# Prompt

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

# Buggy Code

```python
def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    longest_streak = 1
    current_streak = 1
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
                
    return max(longest_streak, current_streak)
```

# Solution

```python
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
```

**Feedback**:
The buggy code sorts the array, which takes `O(n log n)` time, violating the `O(n)` requirement. 
By converting the array to a hash set, we can achieve `O(1)` lookups. We then iterate through the set, and to avoid redundant work, we only start tracking a sequence if it's the start of one (i.e., `num - 1` is not in the set). The inner loop will only iterate exactly `n` times across the whole array in total, giving an overall `O(n)` time complexity.
