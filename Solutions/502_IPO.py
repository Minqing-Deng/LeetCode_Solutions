import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        maxProfit = []  # store the profit that we can afford

        # store all the capitals initially
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for _ in range(k):

            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)

            if not maxProfit:
                break

            w += -1 * heapq.heappop(maxProfit)

        return w
