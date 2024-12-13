from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0

        # # Initialize variables to track the maximum profit
        # # after the first and second transactions
        # first_buy = float('-inf')
        # first_sell = 0
        # second_buy = float('-inf')
        # second_sell = 0

        # for price in prices:
        #     # Update the profits in order
        #     first_buy = max(first_buy, -price)         # Max profit after first buy
        #     first_sell = max(first_sell, first_buy + price)  # Max profit after first sell
        #     second_buy = max(second_buy, first_sell - price) # Max profit after second buy
        #     second_sell = max(second_sell, second_buy + price) # Max profit after second sell

        # return second_sell

        days = len(prices)
        trans = 2
        if days == 0:
            return 0

        # Initialize the dp table
        dp = [[0] * days for _ in range(trans + 1)]

        for i in range(1, trans + 1):  # Transactions
            max_profit_so_far = -prices[0]
            for j in range(1, days):  # Days
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_profit_so_far)
                max_profit_so_far = max(max_profit_so_far, dp[i - 1][j] - prices[j])

        return dp[trans][days - 1]