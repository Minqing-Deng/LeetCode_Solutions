from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)
        visited = set()

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(node, prev):

            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n