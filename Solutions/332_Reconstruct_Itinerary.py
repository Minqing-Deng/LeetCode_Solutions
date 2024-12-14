from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj or len(adj[src]) == 0:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res

        # adj = defaultdict(list)
        # for src, dst in sorted(tickets)[::-1]:
        #     adj[src].append(dst)

        # res = []
        # def dfs(src):
        #     while adj[src]:
        #         dst = adj[src].pop()
        #         dfs(dst)
        #     res.append(src)

        # dfs('JFK')
        # return res[::-1]