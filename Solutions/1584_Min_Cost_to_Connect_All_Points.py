from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = defaultdict(list)  # index: list of other points [distance, index]
        for i in range(n - 1):
            xi, yi = points[i][0], points[i][1]
            for j in range(i + 1, n):
                xj, yj = points[j][0], points[j][1]
                distance = abs(xi - xj) + abs(yi - yj)
                edges[i].append([distance, j])
                edges[j].append([distance, i])

        res = 0
        visited = set()
        minHeap = [[0, 0]]

        while len(visited) < n:
            d, p = heapq.heappop(minHeap)
            if p in visited:
                continue
            res += d
            visited.add(p)
            for nd, np in edges[p]:
                if np not in visited:
                    heapq.heappush(minHeap, [nd, np])

        return res