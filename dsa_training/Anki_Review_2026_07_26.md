# Anki Review - 2026-07-26

## Algorithm: Binary Search (Overflow Prevention)
- **Concept**: Binary Search is used to find a target value in a sorted array in O(log n) time.
- **Overflow Prevention**: Using `left + (right - left) // 2` instead of `(left + right) // 2` prevents integer overflow when `left + right` exceeds the maximum value of an integer in languages with fixed-size integers (e.g., C++, Java). Although Python handles arbitrarily large integers, it's good practice to use the safe formula.
- **Key Takeaway**: Always consider data type limits when performing arithmetic on indices.
