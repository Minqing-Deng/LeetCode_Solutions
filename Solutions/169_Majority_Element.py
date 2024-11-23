from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Sep 23, 2024
        # Boyer-Moore solution
        # Time: O(n), Space: O(1)

        count = 0
        res = nums[0]

        for n in nums:
            if n == res:
                count += 1

            if n != res:
                count -= 1

            if count == 0:
                res = n
                count += 1

        return res

        # # NeetCode:
        # res, count = 0, 0

        # for n in nums:
        #     if count == 0:
        #         res = n
        #     count += (1 if n == res else -1)

        # return res