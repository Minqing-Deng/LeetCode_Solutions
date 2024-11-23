class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        for r in range(numRows):

            increment1 = (numRows-1)*2 # the first and last rows
            for i in range(r, len(s), increment1):
                res += s[i]
                if r > 0 and r < numRows - 1: # the middle rows
                    increment2 = i + ((numRows-1) - r) * 2
                    if increment2 < len(s):
                        res += s[increment2]

        return res