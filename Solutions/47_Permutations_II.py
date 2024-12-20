from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        res = []
        visited = [False] * n

        def dfs(arr):
            if len(arr) == n:
                res.append(arr.copy())
                return

            for i in range(n):
                if i - 1 >= 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                if not visited[i]:
                    arr.append(nums[i])
                    visited[i] = True
                    dfs(arr)
                    arr.pop()
                    visited[i] = False

        dfs([])
        return res