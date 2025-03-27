from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        q = deque()
        q.append("0000")
        visit = set(deadends)
        move = 0

        def children(lock):
            res = []
            for i in range(4):
                newDigit = int(lock[i]) + 1
                if newDigit == 10:
                    newDigit = 0
                res.append(lock[:i] + str(newDigit) + lock[i + 1:])
                newDigit = int(lock[i]) - 1
                if newDigit == -1:
                    newDigit = 9
                res.append(lock[:i] + str(newDigit) + lock[i + 1:])
            return res

        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return move
                for child in children(lock):
                    if child not in visit:
                        visit.add(child)
                        q.append(child)
            move += 1

        return -1