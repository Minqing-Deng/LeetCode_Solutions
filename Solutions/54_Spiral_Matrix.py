from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # rignt, down, left, up
        action = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        row = len(matrix)
        col = len(matrix[0])

        visited = [[0 for _ in range(col)] for _ in range(row)]  # 0: non visited, 1: visited

        r, c = 0, -1

        res = []
        count = 0
        action_index = 0

        while count < row * col:

            new_r, new_c = r + action[action_index][0], c + action[action_index][1]

            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col or visited[new_r][new_c] == 1:
                action_index = (action_index + 1) % 4
                new_r, new_c = r + action[action_index][0], c + action[action_index][1]

            res.append(matrix[new_r][new_c])
            visited[new_r][new_c] = 1
            r, c = new_r, new_c
            count += 1

        return res