class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # True DP Bottom Up solution:
        # Time: O(m*n), Space: O(n)
        dp = [1] * n
        cur_dp = [1] * n

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                cur_dp[c] = dp[c] + cur_dp[c + 1]
            dp = cur_dp

        return dp[0]