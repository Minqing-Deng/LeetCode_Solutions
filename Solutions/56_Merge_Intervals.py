from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda pair: pair[0])

        l = intervals[0][0]
        r = intervals[0][1]

        if len(intervals) == 1:
            return [[l, r]]

        res = []

        i = 1
        while i < len(intervals):
            while i < len(intervals) and r >= intervals[i][0]:
                if r < intervals[i][1]:
                    r = intervals[i][1]
                i += 1
            res.append([l, r])
            if i < len(intervals):
                l = intervals[i][0]
                r = intervals[i][1]

        return res