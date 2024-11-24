from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def findMaxSum(nums):
            maxSum = nums[0]
            curSum = 0

            for num in nums:
                if curSum < 0:
                    curSum = 0
                curSum += num
                maxSum = max(maxSum, curSum)

            return maxSum

        def findMinSum(nums):
            minSum = nums[0]
            curSum = 0

            for num in nums:
                if curSum > 0:
                    curSum = 0
                curSum += num
                minSum = min(minSum, curSum)

            return minSum

        non_circular_maxSum = findMaxSum(nums)

        # If the maximum subarray sum is negative,
        # return it, since this means all numbers are negative
        # If the array consists entirely of negative numbers,
        # the total sum minus the minimum sum would give 0 (or even worse).
        # So in such cases, we return the non-circular maximum sum,
        # as circular wrapping doesn't help when all elements are negative.
        if non_circular_maxSum < 0:
            return non_circular_maxSum
        else:
            total = sum(nums)
            minSum = findMinSum(nums)
            circular_maxSum = total - minSum
            return max(non_circular_maxSum, circular_maxSum)