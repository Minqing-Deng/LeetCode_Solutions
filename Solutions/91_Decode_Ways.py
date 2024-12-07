class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        # Brute Force DFS
        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i <= n - 2:
                if s[i] == "1" or s[i] == "2" and s[i + 1] <= "6":
                    res += dfs(i + 2)

            return res

        return dfs(0)

        # Dynamic Programming Top-Down (Cache)
        cache = {}
        cache[n] = 1

        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i <= n - 2:
                if s[i] == "1" or s[i] == "2" and s[i + 1] <= "6":
                    res += dfs(i + 2)
            cache[i] = res
            return cache[i]

        return dfs(0)

        # Dynamic Programming Bottom-Up
        dp = {}
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            if s[i] != "0":
                dp[i] = dp[i + 1]
            if i <= n - 2:
                if s[i] == "1" or s[i] == "2" and s[i + 1] <= "6":
                    dp[i] += dp[i + 2]
        return dp[0]

        # Dynamic Programming Bottom-Up (Optimal Space)
        dp1 = 0
        dp2 = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp3 = 0
            if s[i] != "0":
                dp3 = dp2
            if i <= n - 2:
                if s[i] == "1" or s[i] == "2" and s[i + 1] <= "6":
                    dp3 += dp1
            temp = dp2
            dp2 = dp3
            dp1 = temp
        return dp3