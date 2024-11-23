from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sep 23, 2024
        # Time: O(n), Space: O(1)
        maxProfit = 0
        lowestPrice = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - lowestPrice
            maxProfit = max(profit, maxProfit)
            lowestPrice = min(prices[i], lowestPrice)

        return maxProfit