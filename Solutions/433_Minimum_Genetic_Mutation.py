from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        # use BFS
        q = deque()
        visit = set()
        q.append(startGene)
        visit.add(startGene)
        genLen = len(startGene)
        gens = ['A', 'C', 'G', 'T']

        mutation = 0

        while q:
            size = len(q)
            for _ in range(size):
                newGen = q.popleft()

                if newGen == endGene:
                    return mutation

                temp = newGen

                for i in range(genLen):
                    char = newGen[i]
                    for gen in gens:
                        if char != gen:
                            # newGen[i] = gen
                            newGen = newGen[:i] + gen + newGen[i + 1:]
                            if newGen in bank and newGen not in visit:
                                q.append(newGen)
                                visit.add(newGen)
                    newGen = temp

            mutation += 1

        return -1