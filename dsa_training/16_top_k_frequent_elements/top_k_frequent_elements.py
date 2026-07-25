from collections import Counter

def topKFrequent(nums, k):
    if not nums:
        return []
    
    count = Counter(nums)
    # Using most_common to get the k most frequent
    # Most common returns a list of tuples (element, count)
    return [item[0] for item in count.most_common(k)]
