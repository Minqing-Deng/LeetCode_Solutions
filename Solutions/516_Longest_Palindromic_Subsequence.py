class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        text1 = s
        text2 = s[::-1]

        def longestCommonSubsequence(text1: str, text2: str) -> int:

            dp = [[0] * len(text2) for _ in range(len(text1))]

            # fill the first row to reduce edge cases:
            index = text2.find(text1[0])
            if index != -1:
                for i in range(index, len(text2)):
                    dp[0][i] = 1

            # fill the first column to reduce edge cases:
            index = text1.find(text2[0])
            if index != -1:
                for i in range(index, len(text1)):
                    dp[i][0] = 1

            for i in range(1, len(text1)):
                for j in range(1, len(text2)):
                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[len(text1) - 1][len(text2) - 1]

        return longestCommonSubsequence(text1, text2)