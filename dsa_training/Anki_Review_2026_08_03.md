# Anki Review 2026-08-03

## Algorithm Practice
- **Problem**: 36. Valid Sudoku
- **Key Concepts**: Hash Set, Matrix Traversal
- **Notes**:
    - Use three hash sets to track seen digits in rows, columns, and 3x3 sub-boxes.
    - Sub-box identification: `(row // 3, col // 3)`.
    - Time complexity is O(1) as the board size is constant (9x9).

## Anki Cards to Add
1. Q: How to identify the 3x3 sub-box index for a cell (r, c) in a 9x9 Sudoku board?
   A: Use `(r // 3, c // 3)`.

2. Q: What is the most efficient way to validate a 9x9 Sudoku board?
   A: Use three hash sets (or boolean arrays) to track occurrences of digits 1-9 in each row, column, and 3x3 sub-box while traversing the board once.
