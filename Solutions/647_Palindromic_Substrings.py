class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        for i in range(len(s)):
            k = 0
            while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
                res += 1
                k += 1

        for i in range(len(s)):
            j = i + 1
            k = 0
            while i - k >= 0 and j + k < len(s) and s[i - k] == s[j + k]:
                res += 1
                k += 1

        return res