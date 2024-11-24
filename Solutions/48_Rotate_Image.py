from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        L, R = 0, len(matrix) - 1
        T, B = 0, len(matrix) - 1

        while L < R:
            for i in range(R-L):
                temp1 = matrix[T+i][R] # store 11
                matrix[T+i][R] = matrix[T][L+i] # space 11 = 5
                temp2 = matrix[B][R-i] # store 16
                matrix[B][R-i] = temp1 # space 16 = 11
                temp1 = matrix[B-i][L] # store 15
                matrix[B-i][L] = temp2 # space 15 = 16
                matrix[T][L+i] = temp1 # space 5 = 15
            L += 1
            R -= 1
            T += 1
            B -= 1