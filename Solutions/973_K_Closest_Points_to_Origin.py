import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        priority_queue = []

        for point in points:
            heapq.heappush(priority_queue, [-(point[0] ** 2 + point[1] ** 2), point])
            if len(priority_queue) > k:
                heapq.heappop(priority_queue)

        return [item[1] for item in priority_queue]