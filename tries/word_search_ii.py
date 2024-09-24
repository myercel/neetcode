"""
Problem No. 212

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        ans, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or board[r][c] not in node.children:
                return

            visit.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.end:
                ans.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(ans)