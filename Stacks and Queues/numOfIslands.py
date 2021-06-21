from typing import List
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = -1
            while q:
                row, col = q.pop()
                dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in dirs:
                    if row + dr in range(len(grid)) and col + dc in range(len(grid[0])) \
                            and grid[row + dr][col + dc] == '1':
                        q.append((row + dr, col + dc))
                        grid[row + dr][col + dc] = -1

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    bfs(i, j)
        return num_islands
