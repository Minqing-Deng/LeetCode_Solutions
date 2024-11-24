from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp = stack.pop()
                res[temp[1]] = i - temp[1]
            stack.append((t, i))

        return res