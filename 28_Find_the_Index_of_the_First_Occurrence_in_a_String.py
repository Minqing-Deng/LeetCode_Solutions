class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        # Brute force solution:
        # Time: O(m*n):
        for h in range(len(haystack) + 1 - len(needle)):
            if haystack[h:h + len(needle)] == needle:
                return h

        return -1