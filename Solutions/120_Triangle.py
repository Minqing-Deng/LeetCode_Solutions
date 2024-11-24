from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # # Brute Force DFS solution:

        # def dfs(triangle):
        #     if not triangle:
        #         return 0

        #     if len(triangle) == 1:
        #         return triangle[0][0]

        #     if len(triangle) == 2:
        #         return triangle[0][0] + min(triangle[1])

        #     left_triangle = []
        #     for i in range(1, len(triangle)):
        #         left_triangle.append(triangle[i][:-1])
        #     right_triangle = []
        #     for i in range(1, len(triangle)):
        #         right_triangle.append(triangle[i][1:])

        #     return triangle[0][0] + min(dfs(left_triangle), dfs(right_triangle))

        # return dfs(triangle)


        # # Cache DFS solution:

        # cache = {}

        # def dfs(r, c):

        #     if r == len(triangle) - 1:
        #         return triangle[r][c]

        #     if r == len(triangle) - 2:
        #         return triangle[r][c] + min(triangle[r+1][c:c+2])

        #     if (r, c) in cache:
        #         return cache[(r, c)]

        #     cache[(r, c)] = triangle[r][c] + min(dfs(r+1,c), dfs(r+1, c+1))

        #     return cache[(r, c)]

        # return dfs(0, 0)


        # True DP Bottom Up solution:
        dp = triangle[-1]
        for r in range(len(triangle)-2, -1, -1):
            cur_dp = []
            for c in range(len(triangle[r])):
                cur_dp.append(triangle[r][c] + min(dp[c], dp[c+1]))
            dp = cur_dp

        return dp[0]