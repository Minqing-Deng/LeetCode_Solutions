from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(i, combination, total):
            if total == target:
                res.append(combination.copy())
                return
            if total > target or i >= len(candidates):
                return

            combination.append(candidates[i])
            backtrack(i+1, combination, total+candidates[i])
            combination.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, combination, total)

        backtrack(0, [], 0)
        return res