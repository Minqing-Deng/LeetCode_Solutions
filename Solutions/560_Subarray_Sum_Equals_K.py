from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        prefixSum = 0
        hashMap = defaultdict(int)
        # Initialize with sum 0 to handle cases where prefix_sum itself is k
        hashMap[0] = 1

        for n in nums:
            prefixSum += n
            diff = prefixSum - k
            # Check if there exists a prefix sum that would form a subarray sum of k
            res += hashMap[diff]
            # Update the count of prefix_sum in the hashmap
            hashMap[prefixSum] += 1

        return res

