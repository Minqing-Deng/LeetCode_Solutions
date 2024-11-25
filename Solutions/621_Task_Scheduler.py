from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}

        for task in tasks:
            if task not in hashMap:
                hashMap[task] = 1
            else:
                hashMap[task] += 1

        maxHeap = [-fre for task, fre in hashMap.items()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                fre = heapq.heappop(maxHeap)
                fre += 1
                if fre < 0:
                    q.append([fre, time + n])
            if q:
                if q[0][1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])

        return time