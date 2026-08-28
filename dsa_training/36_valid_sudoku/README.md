# 36. Valid Sudoku

## Problem
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

## Approach
- Use Hash Sets to keep track of seen numbers in rows, columns, and 3x3 boxes.
- For each cell `(r, c)` with value `val`:
    - Row key: `row_r_val`
    - Column key: `col_c_val`
    - Box key: `box_r/3_c/3_val`
    - If any key exists in the set, return `False`.
    - Otherwise, add the keys to the set.
- Time Complexity: O(1) because the board size is fixed at 9x9.
- Space Complexity: O(1).
