class Solution:
    def reverseWords(self, s: str) -> str:

        res = ""

        i = len(s) - 1

        while i >= 0:

            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:  # all space
                break
            r = i  # the right index of the word

            while i >= 0 and s[i] != " ":
                i -= 1
            l = i + 1  # the left index of the word

            # for j in range(l, r+1):
            #     res += s[j]
            # res += " "

            res += s[l:r + 1] + " "

        return res[:-1]