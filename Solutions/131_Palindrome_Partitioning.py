from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def isPalindrome(arr):
            return arr == arr[::-1]

        def backtrack(i, part):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    backtrack(j + 1, part)
                    part.pop()

        backtrack(0, [])
        return res