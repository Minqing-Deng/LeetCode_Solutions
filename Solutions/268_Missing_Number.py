from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

        # # Time: O(n), Space: O(n)
        # n = len(nums)
        # set1 = set(nums)
        # set2 = set([i for i in range(n+1)])
        # res = list(set2 - set1)

        # return res[0]