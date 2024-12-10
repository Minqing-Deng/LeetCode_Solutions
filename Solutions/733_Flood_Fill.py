from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]

        q = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        if image[sr][sc] != color:
            q.append((sr, sc))

        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr in range(rows) and nc in range(cols) and image[nr][nc] == original_color:
                    q.append((nr, nc))

        return image