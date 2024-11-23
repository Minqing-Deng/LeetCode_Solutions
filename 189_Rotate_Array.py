from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Sep 23, 2024
        # NeetCode solution
        # Time: O(n), Space: O(n)

        res = [0] * len(nums)
        for i, n in enumerate(nums):
            j = (i + k) % len(nums)
            res[j] = nums[i]

        nums[:] = res