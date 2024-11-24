import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = collections.defaultdict(list)

        for equa, value in zip(equations, values):
            a = equa[0]
            b = equa[1]
            adj[a].append([b, value])
            adj[b].append([a, 1 / value])

        # iterative bfs
        def bfs(src, target):
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            if src not in adj or target not in adj:
                return -1

            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)

            return -1

        return [bfs(que[0], que[1]) for que in queries]