from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = True
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    area = 1
                    q = deque()
                    q.append((i, j))
                    while q:
                        r, c = q.popleft()
                        for direction in directions:
                            newR = r + direction[0]
                            newC = c + direction[1]
                            if newR in range(m) and newC in range(n):
                                if grid[newR][newC] == 1 and not visited[newR][newC]:
                                    area += 1
                                    q.append((newR, newC))
                                    visited[newR][newC] = True
                    maxArea = max(maxArea, area)

        return maxArea