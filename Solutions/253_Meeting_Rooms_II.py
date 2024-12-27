from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) <= 1:
            return 1

        intervals.sort(key=lambda x: x.start)

        res = 0
        i = 0

        while i < len(intervals):
            endTime = intervals[i].end
            while i + 1 < len(intervals) and intervals[i + 1].start < endTime:
                i += 1
                endTime = intervals[i].end
            i += 1
            res += 1

        return res