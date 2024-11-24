from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:  # right has the min
                l = m + 1
            else:  # left has the min
                r = m - 1

        return res