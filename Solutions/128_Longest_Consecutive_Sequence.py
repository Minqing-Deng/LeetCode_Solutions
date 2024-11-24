from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # convert it into a set
        # Time: O(n)
        nums = set(nums)

        res = 1

        # Time: O(n)
        for n in nums:
            if n - 1 not in nums:
                temp = n + 1
                length = 1
                while temp in nums:
                    length += 1
                    temp += 1
                res = max(res, length)

        return res