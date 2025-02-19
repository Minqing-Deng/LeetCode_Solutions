from collections import defaultdict
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        dp = defaultdict(lambda: [0] * (k + 1))

        # Iterate over the array in sequence
        for num in nums:
            # Extend subsequence ending with `num` without increasing transitions
            for j in range(k + 1):
                dp[num][j] += 1

            # Transition from other values to `num` (increase transitions)
            for other in list(dp.keys()):
                if other != num:
                    for j in range(1, k + 1):  # Only consider transitions if j > 0
                        dp[num][j] = max(dp[num][j], dp[other][j - 1] + 1)

            # Start a new subsequence with `num`
            dp[num][0] = max(dp[num][0], 1)

        # Find the maximum length across all values with at most k transitions
        max_length = 0
        for num in dp:
            for j in range(k + 1):
                max_length = max(max_length, dp[num][j])

        return max_length