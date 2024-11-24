from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(r, c, k):

            if r not in range(rows) or c not in range(cols) or board[r][c] != word[k] or (r, c) in visit:
                return False

            if k == len(word) - 1:
                return True

            visit.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                if dfs(nr, nc, k + 1):
                    return True
            visit.remove((r, c))

            return False

        # count = defaultdict(int, sum(map(Counter, board), Counter()))
        # if count[word[0]] > count[word[-1]]:
        #     word = word[::-1]

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False