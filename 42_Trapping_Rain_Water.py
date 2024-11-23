from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        maxL = 0
        maxR = 0

        l = 0
        r = len(height) - 1

        res = 0

        while l <= r:
            if maxL <= maxR:
                temp = maxL - height[l]
                if temp >= 0:
                    res += temp
                maxL = max(maxL, height[l])
                l += 1
            else:
                temp = maxR - height[r]
                if temp >= 0:
                    res += temp
                maxR = max(maxR, height[r])
                r -= 1

        return res