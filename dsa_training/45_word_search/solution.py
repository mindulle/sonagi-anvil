from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word, return true if word exists in the grid.
        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
        The same letter cell may not be used more than once.
        """
        if not board or not board[0]:
            return False
            
        m, n = len(board), len(board[0])
        
        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[index]:
                return False
                
            temp = board[r][c]
            board[r][c] = '#'
            
            res = (dfs(r+1, c, index+1) or
                   dfs(r-1, c, index+1) or
                   dfs(r, c+1, index+1) or
                   dfs(r, c-1, index+1))
                   
            board[r][c] = temp
            return res
            
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                    
        return False
