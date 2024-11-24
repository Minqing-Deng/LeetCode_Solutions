from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # [[1, 6], [2, 8], [7, 12], [10, 16]]
        points.sort(key=lambda pair: pair[0])

        res = len(points)
        i = 1
        prev = points[0]

        while i < len(points):

            curr = points[i]

            if curr[0] <= prev[1]:
                prev = [curr[0], min(prev[1], curr[1])]
                res -= 1

            else:
                prev = curr

            i += 1

        return res