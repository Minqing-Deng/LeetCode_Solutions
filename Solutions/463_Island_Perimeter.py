from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        res = 0
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    for dr, dc in d:
                        nr = r + dr
                        nc = c + dc
                        if nr not in range(row):
                            res += 1
                        if nc not in range(col):
                            res += 1
                        if nr in range(row) and nc in range(col) and grid[nr][nc] == 0:
                            res += 1

        return res