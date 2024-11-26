from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        minute = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            addMinute = False
            for _ in range(len(q)):
                r, c = q.popleft()
                for direction in directions:
                    newR = r + direction[0]
                    newC = c + direction[1]
                    if newR in range(m) and newC in range(n):
                        if grid[newR][newC] == 1:
                            addMinute = True
                            grid[newR][newC] = 2
                            q.append((newR, newC))
            if addMinute:
                minute += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1

        return minute