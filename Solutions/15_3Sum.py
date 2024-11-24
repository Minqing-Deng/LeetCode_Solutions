from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums = sorted(nums)

        for i in range(len(nums)):

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:

                threeSum = nums[i] + nums[j] + nums[k]

                if threeSum < 0:
                    j += 1
                elif threeSum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
                    while nums[k + 1] == nums[k] and j < k:
                        k -= 1

        return res