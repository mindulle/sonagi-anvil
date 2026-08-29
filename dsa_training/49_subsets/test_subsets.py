from subsets import subsets

def test_subsets_basic():
    nums = [1, 2, 3]
    result = subsets(nums)
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    # Sort both to compare regardless of order
    result_sorted = sorted([sorted(x) for x in result])
    expected_sorted = sorted([sorted(x) for x in expected])
    assert result_sorted == expected_sorted

def test_subsets_empty():
    nums = []
    result = subsets(nums)
    expected = [[]]
    assert result == expected

def test_subsets_single():
    nums = [0]
    result = subsets(nums)
    expected = [[], [0]]
    result_sorted = sorted([sorted(x) for x in result])
    expected_sorted = sorted([sorted(x) for x in expected])
    assert result_sorted == expected_sorted
