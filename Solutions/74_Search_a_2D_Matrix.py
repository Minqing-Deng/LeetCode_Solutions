from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0  # the index of the top row
        b = len(matrix) - 1  # the index of the bottom row
        i = -1

        while t <= b:
            m1 = (t + b) // 2  # the index of the middle row
            if target < matrix[m1][0]:
                b = m1 - 1
            elif target > matrix[m1][-1]:
                t = m1 + 1
            else:
                i = m1  # the index of row to check
                break

        if i == -1:  # if i is not assigned anything, no row is found
            return False

        l = 0  # the index of the left column
        r = len(matrix[i]) - 1  # the index of the right column

        while l <= r:
            m2 = (l + r) // 2  # the index of the middle column

            if target < matrix[i][m2]:
                r = m2 - 1
            elif target > matrix[i][m2]:
                l = m2 + 1
            else:
                return True

        return False
