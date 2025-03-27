from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        totalSum = sum(nums)
        if totalSum % k != 0:
            return False
        target = totalSum // k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backtrack(i, k, subSum):
            if k == 1:
                return True

            if subSum == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if not used[j] and nums[j] + subSum <= target:
                    used[j] = True
                    if backtrack(j + 1, k, subSum + nums[j]):
                        return True
                    used[j] = False
                    if subSum == 0:
                        break
            return False

        return backtrack(0, k, 0)