from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, arr):
            if i == len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            helper(i + 1, arr)
            arr.pop()
            helper(i + 1, arr)

        helper(0, [])

        return res