from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            if l == r:  # Only one element, so it's the peak
                return l

            m = (l + r) // 2

            # If middle element is greater than the right neighbor, look left
            if nums[m] > nums[m + 1]:
                r = m

            else: # Otherwise, look right
                l = m + 1