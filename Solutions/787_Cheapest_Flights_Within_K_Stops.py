from collections import deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # hashMap = defaultdict(list) # from: list of [price, to]

        # for f, t, p in flights:
        #     hashMap[f].append([p, t])

        # minHeap = [[0, k+1, src]] # frontier: price, stop, city

        # while minHeap:
        #     priceSoFar, stop, city = heapq.heappop(minHeap)
        #     if city == dst:
        #         return priceSoFar
        #     if stop > 0:
        #         for neiP, nei in hashMap[city]:
        #             heapq.heappush(minHeap, [priceSoFar + neiP, stop - 1, nei])

        # return -1

        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue

            for nei, w in adj[node]:
                nextCost = cst + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1