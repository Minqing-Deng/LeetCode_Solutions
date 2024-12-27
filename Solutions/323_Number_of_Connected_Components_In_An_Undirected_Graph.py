from collections import defaultdict, deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        res = 0
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                n = q.popleft()
                visited.add(n)
                for nei in adj[n]:
                    if nei not in visited:
                        q.append(nei)

        for node in range(n):
            if node not in visited:
                res += 1
                bfs(node)

        return res