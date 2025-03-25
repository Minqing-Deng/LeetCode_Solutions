# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        # Use binary search to find the peak of the array
        # The condition of the peak is that the left and right elements of the peak
        # are both smaller than the peak
        # When you finally find the peak,
        # uew binary again to find the target on the left portion, and then the right portion.

        n = mountainArr.length()

        # Find the peak
        l = 1
        r = n - 2
        peak = -1
        while l <= r:
            m = l + (r - l) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid > right:
                peak = m
                break
            elif left < mid < right:
                l = m + 1
            else:
                r = m - 1

        # Find the left portion
        l = 0
        r = peak
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        # Find the right portion
        l = peak + 1
        r = n - 1
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target:
                l = m + 1
            else:
                r = m - 1
        return -1