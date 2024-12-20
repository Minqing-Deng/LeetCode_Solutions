from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True

            elif nums[l] == nums[m] and nums[m] == nums[r]:
                if len(set(nums[l:m+1])) == 1:
                    l = m + 1
                else:
                    r = m - 1

            elif nums[l] <= nums[m]: # left part is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            elif nums[m] <= nums[r]: # right part is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False