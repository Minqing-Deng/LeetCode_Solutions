from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Keep track of rows and columns that need to be zeroed
        zero_rows = set()
        zero_cols = set()

        # First pass: Identify rows and columns that should be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Second pass: Zero out identified rows
        for r in zero_rows:
            for c in range(cols):
                matrix[r][c] = 0

        # Third pass: Zero out identified columns
        for c in zero_cols:
            for r in range(rows):
                matrix[r][c] = 0