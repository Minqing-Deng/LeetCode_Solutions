from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        n = len(matchsticks)
        length = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        def backtrack(i, l, r, t, b):
            if i == n and l == length and r == length and t == length and b == length:
                return True
            if l > length or r > length or t > length or b > length:
                return False

            if (backtrack(i + 1, l + matchsticks[i], r, t, b)
                    or backtrack(i + 1, l, r + matchsticks[i], t, b)
                    or backtrack(i + 1, l, r, t + matchsticks[i], b)
                    or backtrack(i + 1, l, r, t, b + matchsticks[i])):
                return True
            return False

        return backtrack(0, 0, 0, 0, 0)