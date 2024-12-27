from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])

        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            r, c, distance = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr in range(m) and nc in range(n) and grid[nr][nc] != -1 and grid[nr][nc] > distance + 1:
                    grid[nr][nc] = distance + 1
                    q.append((nr, nc, distance + 1))