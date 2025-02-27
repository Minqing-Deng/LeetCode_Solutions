from collections import defaultdict
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        m = len(words)
        n = len(words[0])
        hashMap = [defaultdict(int) for _ in range(n)]
        for w in words:
            for i, c in enumerate(w):
                hashMap[i][c] += 1

        cache = {}
        def dfs(i, k):
            if i == len(target):
                return 1
            if k == n:
                return 0
            if (i, k) in cache:
                return cache[(i, k)]

            cache[(i, k)] = hashMap[k][target[i]] * dfs(i + 1, k + 1)
            cache[(i, k)] += dfs(i, k + 1)

            return cache[(i, k)] % mod

        return dfs(0, 0)