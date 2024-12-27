from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # rignt, down, left, up
        action = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        res = [[-1 for _ in range(n)] for _ in range(n)]  # -1: non visited

        r, c = 0, -1

        count = 0
        action_index = 0
        num = 1

        while count < n * n:

            new_r, new_c = r + action[action_index][0], c + action[action_index][1]

            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n or res[new_r][new_c] != -1:
                action_index = (action_index + 1) % 4
                new_r, new_c = r + action[action_index][0], c + action[action_index][1]

            res[new_r][new_c] = num
            num += 1
            r, c = new_r, new_c
            count += 1

        return res