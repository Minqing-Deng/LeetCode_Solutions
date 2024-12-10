from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        # Create a result matrix initialized with a large value
        res = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # Step 1: Initialize the queue with all 0 cells
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    res[r][c] = 0
                    queue.append((r, c))

        # Step 2: Directions for moving in the matrix
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Step 3: BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check boundaries and update if a shorter distance is found
                if 0 <= nr < rows and 0 <= nc < cols:
                    if res[nr][nc] > res[r][c] + 1:
                        res[nr][nc] = res[r][c] + 1
                        queue.append((nr, nc))

        return res