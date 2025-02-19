import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        Time Complexity:
        Building the heap: O(n)
        Each operation: O(logn)
        Total time complexity: O(n+klogn)
        """
        minHeap = [-x for x in piles]
        heapq.heapify(minHeap)

        for _ in range(k):
            value = -1 * (heapq.heappop(minHeap))
            value = -1 * (value - int(value / 2))
            heapq.heappush(minHeap, value)

        return -1 * sum(minHeap)

