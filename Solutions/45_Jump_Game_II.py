from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        # Sep 23, 2024
        # Neetcode BFS solution
        # Time: O(n)

        l = 0
        r = 0
        count = 0

        while r < len(nums) - 1:
            temp = r
            for i in range(l, r + 1):
                r = max(r, i + nums[i])
            l = temp + 1
            count += 1

        return count