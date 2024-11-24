from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if (r, c) in visit or board[r][c] == 'X':
                return

            visit.add((r, c))
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    dfs(nr, nc)

        # Start DFS from 'O's on the edges
        for r in range(rows):
            for c in [0, cols - 1]:  # Left and right edges
                if board[r][c] == 'O':
                    dfs(r, c)
        for r in [0, rows - 1]:  # Top and bottom edges
            for c in range(cols):
                if board[r][c] == 'O':
                    dfs(r, c)

        # Replace all unvisited 'O's with 'X'
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and board[r][c] == 'O':
                    board[r][c] = 'X'

        # # unsuccessful try:
        # if not board:
        #     return board

        # rows = len(board)
        # cols = len(board[0])
        # visit = set()
        # directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # def dfs(r, c):
        #     if r in [0, rows-1] or c in [0, cols-1]:
        #         return

        #     isTurnX = True
        #     for direction in directions:
        #         nr = r + direction[0]
        #         nc = c + direction[1]
        #         if (board[nr][nc] == "O" and (nr, nc) not in visit):
        #             isTurnX = False

        #     if isTurnX:
        #         board[r][c] = "X"
        #         return

        #     visit.add((r, c))
        #     for direction in directions:
        #         nr = r + direction[0]
        #         nc = c + direction[1]
        #         if board[nr][nc] == "O" and (nr, nc) not in visit:
        #             dfs(nr, nc)

        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == "O" and (r, c) not in visit:

        #             dfs(r, c)

        # return board