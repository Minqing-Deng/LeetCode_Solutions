from collections import defaultdict, deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:

        adj = defaultdict(list)
        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        def bfs(start, end):
            q = deque()
            q.append(start)
            visit = set()
            visit.add(start)
            while q:
                c = q.popleft()
                if c == end:
                    return True
                for child in adj[c]:
                    if child not in visit:
                        q.append(child)
                        visit.add(child)
            return False

        res = []
        for c1, c2 in queries:
            res.append(bfs(c1, c2))

        return res