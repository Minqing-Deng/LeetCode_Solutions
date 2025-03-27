from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        hashMap = {}
        for i, c in enumerate(order):
            hashMap[c] = i

        if len(words) <= 1:
            return True

        i = 1
        while i < len(words):
            minL = min(len(words[i - 1]), len(words[i]))
            if words[i - 1][:minL] == words[i][:minL] and len(words[i - 1]) > len(words[i]):
                return False

            for j in range(minL):
                if hashMap[words[i - 1][j]] > hashMap[words[i][j]]:
                    return False
                elif hashMap[words[i - 1][j]] < hashMap[words[i][j]]:
                    break

            i += 1

        return True