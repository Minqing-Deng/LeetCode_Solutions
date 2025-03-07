from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = l + (r - l) // 2
            if not check(m):
                l = m + 1
            else:
                r = m - 1

        return l