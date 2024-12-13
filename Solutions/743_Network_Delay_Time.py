import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        res = 0
        hashMap = defaultdict(list)  # source node: list of [weight, target node]...

        for time in times:
            s, t, w = time
            hashMap[s].append([w, t])

        minHeap = [[0, k]]

        visited = set()

        while minHeap:
            weightSoFar, node = heapq.heappop(minHeap)
            if node not in visited:
                res = weightSoFar
                visited.add(node)
                for neiW, nei in hashMap[node]:
                    if nei not in visited:
                        heapq.heappush(minHeap, [weightSoFar + neiW, nei])

        return res if len(visited) == n else -1