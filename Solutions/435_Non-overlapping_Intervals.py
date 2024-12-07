from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        res = 0
        start1 = intervals[0][0]
        end1 = intervals[0][1]
        i = 1

        while i < len(intervals):
            start2 = intervals[i][0]
            end2 = intervals[i][1]
            if start2 < end1:
                res += 1
                if end2 < end1:
                    start1 = start2
                    end1 = end2
            else:
                start1 = start2
                end1 = end2
            i += 1

        return res