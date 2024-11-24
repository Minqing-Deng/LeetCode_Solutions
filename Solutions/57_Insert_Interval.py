from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        l = len(intervals)
        r = -1
        res = []

        if newInterval[1] < intervals[0][0]:
            res.append(newInterval)
            res += intervals
            return res

        if newInterval[0] > intervals[-1][1]:
            res += intervals
            res.append(newInterval)
            return res

        while l - 1 >= 0 and newInterval[0] <= intervals[l - 1][1]:
            l -= 1

        while r + 1 < len(intervals) and newInterval[1] >= intervals[r + 1][0]:
            r += 1

        combine = [min(intervals[l][0], newInterval[0]), max(intervals[r][1], newInterval[1])]

        res += intervals[:l]
        res.append(combine)
        res += intervals[r + 1:]

        return res