from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # # NeetCode solution
        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount + 1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a - c])
        # return dp[amount] if dp[amount] != amount + 1 else -1


        # My 2 dimensional DP solution
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]

        # fill the first column and row to reduce edge cases:
        for i in range(len(coins)):
            dp[i][0] = 0
        for a in range(1, amount+1):
            if a - coins[0] >= 0:
                dp[0][a] = 1 + dp[0][a - coins[0]]

        for c in range(1, len(coins)):
            for a in range(1, amount+1):
                if a - coins[c] >= 0:
                    dp[c][a] = min(dp[c-1][a], 1 + dp[c][a - coins[c]])
                else:
                    dp[c][a] = dp[c-1][a]

        return dp[len(coins)-1][amount] if dp[len(coins)-1][amount] != float('inf') else -1