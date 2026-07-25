import pytest
from merge_sorted_array import Solution

def test_merge_sorted_array():
    sol = Solution()
    
    # Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]
    
    # Case 2: nums1 has 0 elements initialized
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1]
    
    # Case 3: nums2 has 0 elements initialized
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1]
