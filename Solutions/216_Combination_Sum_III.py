from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        nums = [num for num in range(1, 10)]

        def dfs(i, arr):
            if len(arr) == k and sum(arr) == n:
                res.append(arr.copy())
                return

            if i >= len(nums) or len(arr) > k or sum(arr) > n:
                return

            arr.append(nums[i])
            dfs(i + 1, arr)
            arr.pop()
            dfs(i + 1, arr)

        dfs(0, [])
        return res