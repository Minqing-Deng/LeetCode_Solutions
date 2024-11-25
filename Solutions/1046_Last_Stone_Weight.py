import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x != y:
                y = y - x
                heapq.heappush(max_heap, -y)
        return -max_heap[0] if len(max_heap) == 1 else 0