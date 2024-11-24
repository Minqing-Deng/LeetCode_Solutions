from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # # True DP Bottom Up solution:
        # # Space: m*n
        # rows = len(grid)
        # cols = len(grid[0])

        # dp = [[0] * cols for _ in range(rows)]

        # dp[-1][-1] = grid[-1][-1]
        # for c in range(len(grid[0])-2, -1, -1):
        #     dp[-1][c] = grid[-1][c] + dp[-1][c+1]

        # for r in range(len(grid)-2, -1, -1):
        #     dp[r][-1] = grid[r][-1] + dp[r+1][-1]

        # for r in range(len(grid)-2, -1, -1):
        #     for c in range(len(grid[0])-2, -1, -1):
        #         dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])

        # return dp[0][0]


        # True DP Bottom Up solution:
        # Space: O(n)

        dp = grid[-1]

        for c in range(len(grid[0])-2, -1, -1):
            dp[c] += dp[c+1]

        for r in range(len(grid)-2, -1, -1):
            cur_dp = grid[r]
            cur_dp[-1] += dp[-1]
            for c in range(len(grid[0])-2, -1, -1):
                cur_dp[c] += min(dp[c], cur_dp[c+1])
            dp = cur_dp

        return dp[0]