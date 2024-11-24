from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

        live_set = set()
        dead_set = set()

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):

                zero_count = 0
                one_count = 0

                for neighbor in neighbors:

                    nei_r = r + neighbor[0]
                    nei_c = c + neighbor[1]

                    # count the 0 and 1 of the neighbors
                    # deal with this: the board is infinite
                    if nei_r < 0 or nei_r >= rows or nei_c < 0 or nei_c >= cols or board[nei_r][nei_c] == 0:
                        zero_count += 1
                    else:
                        one_count += 1

                # apply the rules:
                if board[r][c] == 1 and one_count < 2:
                    dead_set.add((r, c))
                elif board[r][c] == 1 and (one_count == 2 or one_count == 3):
                    live_set.add((r, c))
                elif board[r][c] == 1 and one_count > 3:
                    dead_set.add((r, c))
                elif board[r][c] == 0 and one_count == 3:
                    live_set.add((r, c))

        for grid in live_set:
            board[grid[0]][grid[1]] = 1

        for grid in dead_set:
            board[grid[0]][grid[1]] = 0