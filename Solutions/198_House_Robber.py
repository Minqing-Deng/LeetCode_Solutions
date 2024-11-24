from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # # Brute Force DFS solution:
        # def helper(nums):
        #     if not nums:
        #         return 0

        #     return max(nums[0] + helper(nums[2:]), helper(nums[1:]))

        # return helper(nums)

        # # Cache DFS solution:
        # cache = [-1] * len(nums)

        # def helper(i):
        #     if i >= len(nums):
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]

        #     cache[i] = max(nums[i] + helper(i+2), helper(i+1))
        #     return cache[i]

        # return helper(0)

        # True DP solution:
        preTwo = 0
        preOne = 0

        i = 0
        while i < len(nums):
            temp = max(nums[i] + preTwo, preOne)
            preTwo = preOne
            preOne = temp
            i += 1
        return preOne