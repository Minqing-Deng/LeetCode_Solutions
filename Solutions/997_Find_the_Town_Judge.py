from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        adj = defaultdict(set)

        for p1, p2 in trust:
            adj[p1].add(p2)

        if len(adj.keys()) != n - 1:
            return -1

        judge = list(set(range(1, n + 1)) - set(adj.keys()))[0]

        for trusts in adj.values():
            if judge not in trusts:
                return -1

        return judge