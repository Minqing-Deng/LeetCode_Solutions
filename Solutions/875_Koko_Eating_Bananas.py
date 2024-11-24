from typing import List

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search solution:
        # The K is in the range:[1, ..., max(piles)]
        # Time: O(log(max(p)) * len(p))
        minK = 1
        maxK = max(piles)
        res = maxK
        while minK <= maxK:
            k = (minK + maxK) // 2
            needHours = 0
            for p in piles:
                time = math.ceil(float(p) / k)
                needHours += time
            if needHours <= h:
                res = k
                maxK = k - 1
            elif needHours > h:
                minK = k + 1
        return res


        # # Brute Force solution:
        # # The K is in the range:[1, ..., max(piles)]
        # # Time: O(max(p) * len(p))
        # k = 1

        # while True:
        #     needHours = 0
        #     for p in piles:
        #         time = p // k
        #         if p % k > 0:
        #             time += 1
        #         needHours += time
        #     if needHours <= h:
        #         break
        #     else:
        #         k += 1

        # return k