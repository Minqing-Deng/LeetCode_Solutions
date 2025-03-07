from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        # Binary search problem
        # Seaching space: [max(nums), sum(nums)]

        def canSplit(largest):
            curSum = 0
            subArr = 1
            for n in nums:
                curSum += n
                if curSum > largest:
                    subArr += 1
                    if subArr > k:
                        return False
                    curSum = n
            return True

        l = max(nums)
        r = sum(nums)

        while l <= r:
            m = l + (r - l) // 2
            if canSplit(m):
                r = m - 1
            else:
                l = m + 1
        return l
