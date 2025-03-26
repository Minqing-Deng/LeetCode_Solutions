import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda x: x[1])
        minHeap = []
        curPass = 0

        for trip in trips:
            passenger, start, end = trip
            while minHeap and minHeap[0][0] <= start:
                end2, passenger2 = heapq.heappop(minHeap)
                curPass -= passenger2
            curPass += passenger
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, (end, passenger))

        return True