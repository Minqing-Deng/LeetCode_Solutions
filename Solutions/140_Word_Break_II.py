from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []

        def dfs(i, arr):

            if i == len(s):
                res.append(" ".join(arr))
                return

            for w in wordDict:
                wLen = len(w)
                if i + wLen <= len(s):
                    if s[i:i + wLen] == w:
                        arr.append(w)
                        dfs(i + wLen, arr)
                        arr.pop()

        dfs(0, [])
        return res