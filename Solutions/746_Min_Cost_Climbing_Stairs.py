from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two = cost[-1]
        one = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            temp = two
            two = one
            one = cost[i] + min(one, temp)

        return min(one, two)