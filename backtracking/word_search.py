"""
Problem No. 79

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, curr):
            # curr = curr length of the constructed string
            if curr == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or word[curr] != board[r][c] or (r, c) in path:
                return False

            path.add((r,c)) 
            ans = (dfs(r+1, c, curr+1) or
                    dfs(r-1, c, curr+1) or
                    dfs(r, c+1, curr+1) or
                    dfs(r, c-1, curr+1))

            path.remove((r, c))
            return ans
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

        # O(n * m * 4^n)