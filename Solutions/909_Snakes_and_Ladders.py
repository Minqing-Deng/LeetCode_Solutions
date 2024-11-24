from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        q = deque()
        visit = set()
        visit.add(1)
        q.append(1)
        move = 0

        while q:

            size = len(q)

            for _ in range(size):
                num = q.popleft()
                if num == n * n:
                    return move

                for i in range(1, 7):

                    # new num
                    next_num = num + i

                    if next_num > n * n:
                        continue

                    r = n - ((next_num - 1) // n) - 1  # the row number
                    if r % 2 == ((n % 2) + 1) % 2:  # different row has different col number
                        c = (next_num - 1) % n
                    else:
                        c = n - ((next_num - 1) % n) - 1

                    if board[r][c] == -1:
                        if next_num not in visit:
                            q.append(next_num)
                            visit.add(next_num)
                    else:
                        if board[r][c] not in visit:
                            q.append(board[r][c])
                            visit.add(board[r][c])

            move += 1

        return -1