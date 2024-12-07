from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tempMax = curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(num * tempMax,  num * curMin, num)
            res = max(res, curMax)
        return res