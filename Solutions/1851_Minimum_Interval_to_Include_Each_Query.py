import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        hashMap = {}
        for i, query in enumerate(queries):
            if query in hashMap:
                hashMap[query].append(i)
            else:
                hashMap[query] = [i]
        queries.sort()
        res = [0] * len(queries)

        i = 0
        minHeap = []

        for query in queries:
            while i < len(intervals) and intervals[i][0] <= query:
                # (size, endpoint)
                heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if not minHeap:
                for index in hashMap[query]:
                    res[index] = -1
            else:
                for index in hashMap[query]:
                    res[index] = minHeap[0][0]

        return res