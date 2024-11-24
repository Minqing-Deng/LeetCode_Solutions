from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        # # BFS solution, only beat 5.02% time complexity :(
        # adj = collections.defaultdict(list)

        # for pre in prerequisites:
        #     c0 = pre[0]
        #     c1 = pre[1]
        #     adj[c0].append(c1)

        # def bfs(c):

        #     q, visit = deque(), set()
        #     q.append(c)

        #     while q:
        #         c2 = q.popleft()
        #         for pre in adj[c2]:
        #             if pre == c:
        #                 return False
        #             if pre not in visit:
        #                 q.append(pre)
        #                 visit.add(pre)

        #     return True

        # return all([bfs(c) for c in range(numCourses)])