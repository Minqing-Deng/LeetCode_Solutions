from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Sep 23, 2024
        # Time: O(n), Space: O(1)
        maxP = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                maxP = maxP + (prices[i + 1] - prices[i])

        return maxP