from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        # # Cache DFS solution:
        # # Space: O(2*n)
        # dp = {}
        # # i = index, even = true/false, curNum = current number
        # def dfs(i, even):
        #     if i >= len(nums):
        #         return 0

        #     if (i, even) in dp:
        #         return dp[(i, even)]

        #     curNum = nums[i] if even else -1 * nums[i]
        #     dp[(i, even)] = max(curNum + dfs(i+1, not even), dfs(i+1, even))

        #     return dp[(i, even)]

        # return dfs(0, True)


        # True DP solution:
        # Space: O(1)
        sumEven = 0
        sumOdd = 0

        for i in range(len(nums) - 1, -1, -1):
            # rightnow is even (+)
            # compare use i (next will be odd) or not use i (next will be even)
            tempEven = max(nums[i] + sumOdd, sumEven)
            # rightnow is odd (-)
            # compare use i (next will be even) or not use i (next will be odd)
            tempOdd = max(-nums[i] + sumEven, sumOdd)
            sumEven = tempEven
            sumOdd = tempOdd

        return sumEven