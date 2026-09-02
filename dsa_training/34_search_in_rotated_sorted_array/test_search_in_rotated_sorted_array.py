import pytest
from search_in_rotated_sorted_array import Solution

def test_search():
    sol = Solution()
    
    # Standard case
    assert sol.search([4,5,6,7,0,1,2], 0) == 4
    
    # Not found
    assert sol.search([4,5,6,7,0,1,2], 3) == -1
    
    # Empty
    assert sol.search([], 0) == -1
    
    # Single element
    assert sol.search([1], 1) == 0
    assert sol.search([1], 0) == -1
    
    # Sorted
    assert sol.search([1,3,5], 5) == 2
    
    # Rotated
    assert sol.search([3,1], 1) == 1
