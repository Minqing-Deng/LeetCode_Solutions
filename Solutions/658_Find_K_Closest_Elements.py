from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)
        l = 0
        r = n - 1

        # find the index of element that is equal to or smaller than the x
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] <= x:
                l = m + 1
            else:
                r = m - 1

        if r == -1:
            index = 0
        elif l < n and abs(arr[r] - x) > abs(arr[l] - x):
            index = l
        else:
            index = r

        count = 1
        l = index
        r = index

        while count < k:
            if l - 1 < 0:
                r += 1
            elif r + 1 > n - 1:
                l -= 1
            elif abs(arr[r + 1] - x) < abs(arr[l - 1] - x):
                r += 1
            else:
                l -= 1
            count += 1

        return arr[l:r + 1]