from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
        return the number of islands.
        """
        if not grid:
            return 0
            
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    # Iterative DFS using a stack to avoid RecursionError
                    stack = [(i, j)]
                    grid[i][j] = '0' # mark as visited
                    
                    while stack:
                        r, c = stack.pop()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                stack.append((nr, nc))
                                grid[nr][nc] = '0' # mark as visited early
                                
        return count
