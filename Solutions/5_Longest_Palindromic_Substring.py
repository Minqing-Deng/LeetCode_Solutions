class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = 1
        res = s[0]

        for i in range(len(s)):
            k = 1
            temp = 1
            while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
                temp += 2
                if temp > longest:
                    res = s[i - k:i + k + 1]
                    longest = temp
                k += 1

        for i in range(len(s)):
            j = i + 1
            k = 0
            temp = 0
            while i - k >= 0 and j + k < len(s) and s[i - k] == s[j + k]:
                temp += 2
                if temp > longest:
                    res = s[i - k:j + k + 1]
                    longest = temp
                k += 1

        return res