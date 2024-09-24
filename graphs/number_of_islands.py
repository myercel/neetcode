"""
Problem No. 200

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
all four edges of the grid are all surrounded by water.

Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == "1") and ((r,c) not in visit):
                        queue.append((r,c))
                        visit.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands