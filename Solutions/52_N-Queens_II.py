class Solution:
    def totalNQueens(self, n: int) -> int:

        colSet = set()
        posDiag = set()  # (r + c)
        nagDiag = set()  # (r - c)

        count = 0

        def backTrack(r):

            if r == n:
                nonlocal count
                count += 1
                return

            for c in range(n):
                if c in colSet or (r + c) in posDiag or (r - c) in nagDiag:
                    continue

                colSet.add(c)
                posDiag.add(r + c)
                nagDiag.add(r - c)

                backTrack(r + 1)

                colSet.remove(c)
                posDiag.remove(r + c)
                nagDiag.remove(r - c)

        backTrack(0)
        return count