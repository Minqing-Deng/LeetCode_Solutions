from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for l in range(len(nums) - 1):
        #     for r in range(l + 1, len(nums)):
        #         if nums[r] == target - nums[l]:
        #             return [l, r]

        hashmap = {}  # value: index
        for i, v in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[v] = i