from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        order = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    order[w1[j]].add(w2[j])
                    break

        visit, cycle = set(), set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True

            cycle.add(c)
            for nei in order[c]:
                if not dfs(nei):
                    return False
            cycle.remove(c)
            res.append(c)
            visit.add(c)
            return True

        for c in order:
            if not dfs(c):
                return ""

        res.reverse()
        return "".join(res)