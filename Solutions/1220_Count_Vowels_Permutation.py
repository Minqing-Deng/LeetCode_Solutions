class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a, e, i, o, u = 0, 1, 2, 3, 4
        dp = [[0] * 5 for _ in range(n + 1)]
        dp[1] = [1, 1, 1, 1, 1]

        for r in range(2, n+1):
            dp[r][a] = (dp[r-1][e] + dp[r-1][i] + dp[r-1][u]) % MOD
            dp[r][e] = (dp[r-1][a] + dp[r-1][i]) % MOD
            dp[r][i] = (dp[r-1][e] + dp[r-1][o]) % MOD
            dp[r][o] = dp[r-1][i] % MOD
            dp[r][u] = (dp[r-1][i] + dp[r-1][o]) % MOD

        return sum(dp[n]) % MOD