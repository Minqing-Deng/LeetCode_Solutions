import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        maxHeap = []
        for fre, cha in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if fre != 0:
                heapq.heappush(maxHeap, (fre, cha))

        res = ""
        while maxHeap:
            fre, cha = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == res[-2] == cha:
                if not maxHeap:
                    break
                else:
                    fre2, cha2 = heapq.heappop(maxHeap)
                    res += cha2
                    fre2 += 1
                    if fre2 != 0:
                        heapq.heappush(maxHeap, (fre2, cha2))
                heapq.heappush(maxHeap, (fre, cha))
            else:
                res += cha
                fre += 1
                if fre != 0:
                    heapq.heappush(maxHeap, (fre, cha))

        return res