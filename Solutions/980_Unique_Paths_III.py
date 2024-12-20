from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        zero = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    sr = r
                    sc = c
                if grid[r][c] == 2:
                    er = r
                    ec = c
                if grid[r][c] == 0:
                    zero += 1
        # BFS:
        ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0

        def dfs(r, c, visited):
            nonlocal res
            if r == er and c == ec and len(visited) == zero+2:
                res += 1
                return

            if r == er and c == ec and len(visited) != zero+2:
                return

            for dr, dc in ds:
                nr = r + dr
                nc = c + dc
                if nr in range(m) and nc in range(n) and (nr, nc) not in visited and grid[nr][nc] != -1:
                    visited.add((nr, nc))
                    dfs(nr, nc, visited)
                    visited.remove((nr, nc))

        visited = set()
        visited.add((sr, sc))
        dfs(sr, sc, visited)
        return res