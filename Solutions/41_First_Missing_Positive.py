from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Negative Marking
        # use a negative number to indicate that index+1 number exit
        # first run: set all the non-positive numer to a default value: (n+1)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = (n + 1)

        # second run: mark the num exit in the array at its correct position
        # using negative number to indicate this situation
        for i, num in enumerate(nums):
            if 1 <= abs(num) <= n:
                if nums[abs(num) - 1] > 0:
                    nums[abs(num) - 1] = -nums[abs(num) - 1]

        # third run: loop throught index [1 to n]
        # if the nums[index] is a positive number
        # return that index + 1
        for i in range(1, n + 1):
            if nums[i - 1] > 0:
                return i

        return n + 1