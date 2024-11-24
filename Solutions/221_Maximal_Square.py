from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # True DP Bottom Up solution:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r + 1][c + 1], dp[r + 1][c], dp[r][c + 1])

        maxValue = max(max(row) for row in dp)

        return maxValue * maxValue