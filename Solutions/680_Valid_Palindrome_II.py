class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            return s == s[::-1]

        n = len(s)
        l, r = 0, n-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1]):
                    return True
                else:
                    return False
        return True