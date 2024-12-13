from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days = len(prices)
        trans = k
        if days == 0:
            return 0

        # If k is large enough, it's equivalent to unlimited transactions
        if trans >= days // 2:
            return sum(max(0, prices[i + 1] - prices[i]) for i in range(days - 1))

        # Initialize the dp table
        dp = [[0] * days for _ in range(trans + 1)]

        for i in range(1, trans + 1):  # Transactions
            max_profit_so_far = -prices[0]
            for j in range(1, days):  # Days
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_profit_so_far)
                max_profit_so_far = max(max_profit_so_far, dp[i - 1][j] - prices[j])

        return dp[trans][days - 1]