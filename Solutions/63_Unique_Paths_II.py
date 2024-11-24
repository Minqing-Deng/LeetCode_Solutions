from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # True DP Bottom Up solution:
        # Time: O(m*n), Space: O(n)
        if obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n
        dp[-1] = 1
        for c in range(n - 2, -1, -1):
            if obstacleGrid[-1][c] != 1:
                dp[c] = dp[c + 1]

        for r in range(m - 2, -1, -1):
            cur_dp = [0] * n
            if obstacleGrid[r][-1] != 1:
                cur_dp[-1] = dp[-1]
            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c] != 1:
                    cur_dp[c] = dp[c] + cur_dp[c + 1]
            dp = cur_dp

        return dp[0]