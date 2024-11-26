from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        def bfs(starts):
            visited = set(starts)
            q = deque(visited)
            while q:
                r, c = q.popleft()
                for direction in directions:
                    newR = r + direction[0]
                    newC = c + direction[1]
                    if newR in range(m) and newC in range(n):
                        if heights[r][c] <= heights[newR][newC] and (newR, newC) not in visited:
                            visited.add((newR, newC))
                            q.append((newR, newC))
            return visited

        flow_pacific = bfs(pacific_starts)
        flow_atlantic = bfs(atlantic_starts)

        return list(flow_pacific & flow_atlantic)