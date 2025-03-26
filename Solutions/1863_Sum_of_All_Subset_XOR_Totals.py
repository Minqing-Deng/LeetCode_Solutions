from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(i, subset):
            nonlocal res

            if i >= len(nums):
                total = 0
                for n in subset:
                    total ^= n
                res += total
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return res