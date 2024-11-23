from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Sep 23, 2024
        # NeetCode greedy solution
        # Time: O(n)

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):

            if i + nums[i] >= goal:
                goal = i

        return goal == 0