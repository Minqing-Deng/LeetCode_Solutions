from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        colSet = set()
        posDiag = set()  # (r + c)
        nagDiag = set()  # (r - c)

        board = [["."] * n for _ in range(n)]
        boards = []

        def backTrack(r):

            if r == n:
                copy = ["".join(row) for row in board]
                boards.append(copy)
                return

            for c in range(n):
                if c in colSet or (r + c) in posDiag or (r - c) in nagDiag:
                    continue

                colSet.add(c)
                posDiag.add(r + c)
                nagDiag.add(r - c)
                board[r][c] = "Q"

                backTrack(r + 1)

                colSet.remove(c)
                posDiag.remove(r + c)
                nagDiag.remove(r - c)
                board[r][c] = "."

        backTrack(0)
        return boards