import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort()

        time = tasks[0][0]
        minHeap = []
        i = 0
        res = []

        while i < len(tasks) or minHeap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            if minHeap:
                task = heapq.heappop(minHeap)
                time += task[0]
                res.append(task[1])
            else:
                time = tasks[i][0]

        return res