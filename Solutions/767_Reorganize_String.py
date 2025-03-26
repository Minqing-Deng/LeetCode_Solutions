import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)
        maxHeap = [(-fre, cha) for cha, fre in count.items()]
        heapq.heapify(maxHeap)
        res = ""
        prev = None

        while maxHeap:
            fre, cha = heapq.heappop(maxHeap)
            if prev and prev == cha:
                if not maxHeap:
                    break
                else:
                    fre2, cha2 = heapq.heappop(maxHeap)
                    res += cha2
                    fre2 += 1
                    prev = cha2
                    if fre2 != 0:
                        heapq.heappush(maxHeap, (fre2, cha2))
                heapq.heappush(maxHeap, (fre, cha))
            else:
                res += cha
                fre += 1
                prev = cha
                if fre != 0:
                    heapq.heappush(maxHeap, (fre, cha))

        if len(res) == len(s):
            return res
        else:
            return ""