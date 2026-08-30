# Number of Islands

- **Pattern**: Depth-First Search (DFS) or Breadth-First Search (BFS) on a grid.
- **Key Idea**: Iterate through every cell. When a '1' (land) is found, it's a new island. Increment the count and use DFS/BFS to mark all connected '1's as '0' (visited) so they aren't double-counted.
- **Edge Cases**: Empty grid or 1x1 grid.
- **Complexity**: 
  - Time: O(M * N) since every cell is visited a constant number of times.
  - Space: O(M * N) in the worst case (e.g. all '1's) for the DFS recursion stack.

## Note
- Always check grid bounds before accessing cells.
- Modifying the input grid directly saves O(M * N) space that would otherwise be needed for a `visited` set/array.
