from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hasOdd = False
        res = 0
        char_count = Counter(s)

        for count in char_count.values():
            if count % 2 == 0:
                res += count
            else:
                res += count - 1
                hasOdd = True

        if hasOdd:
            res += 1

        return res