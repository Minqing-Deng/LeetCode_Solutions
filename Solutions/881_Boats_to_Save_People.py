from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0
        r = n-1

        res = 0
        while l <= r:
            if l != r and people[l] + people[r] <= limit:
                l += 1
            r -= 1
            res += 1
        return res