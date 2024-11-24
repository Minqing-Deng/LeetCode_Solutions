from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Sliding window
        l = 0
        minLength = float('inf')
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minLength = min(minLength, (r - l + 1))
                total -= nums[l]
                l += 1

        return 0 if minLength == float('inf') else minLength