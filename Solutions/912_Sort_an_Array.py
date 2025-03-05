from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # merge sort:
        def mergeSort(l, r):
            if l == r:
                return

            m = l + (r - l) // 2

            mergeSort(l, m)
            mergeSort(m + 1, r)
            merge(l, m, r)

        def merge(l, m, r):
            left = nums[l:m + 1]
            right = nums[m + 1:r + 1]

            i, j, k = 0, 0, l
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

        mergeSort(0, len(nums))
        return nums

