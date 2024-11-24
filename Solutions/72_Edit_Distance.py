class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # True DP Bottom Up solution:
        l1 = len(word1)
        l2 = len(word2)

        dp = [[float('inf')] * (l2+1) for _ in range(l1+1)]

        # fill the last row
        temp = l2
        for c in range(l2+1):
            dp[-1][c] = temp
            temp -= 1

        # fill the last column
        temp = l1
        for r in range(l1+1):
            dp[r][-1] = temp
            temp -= 1

        for r in range(l1-1, -1, -1):
            for c in range(l2-1, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]

                else:
                    dp[r][c] = 1 + min(dp[r][c+1], dp[r+1][c], dp[r+1][c+1])

        return dp[0][0]
