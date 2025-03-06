from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                l = j + 1
                r = n - 1
                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fourSum < target:
                        l += 1
                    elif fourSum > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l-1] == nums[l] and l < r:
                            l += 1

        return res