from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sumMatrix = [[0] * n for _ in range(m)]
        for r in range(m):
            prefix = 0
            for c in range(n):
                prefix += matrix[r][c]
                above = self.sumMatrix[r-1][c] if r-1 >= 0 else 0
                self.sumMatrix[r][c] = above + prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        above = self.sumMatrix[row1-1][col2] if row1-1 >= 0 else 0
        left = self.sumMatrix[row2][col1-1] if col1-1 >= 0 else 0
        topleft = self.sumMatrix[row1-1][col1-1] if row1-1 >= 0 and col1-1 >= 0 else 0
        return self.sumMatrix[row2][col2] - above - left + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)