from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)

        if n % groupSize != 0:
            return False

        hashMap = {}
        for h in hand:
            if h in hashMap:
                hashMap[h] += 1
            else:
                hashMap[h] = 1

        minHeap = []
        for h in hashMap:
            heapq.heappush(minHeap, h)

        count = 0
        while count < n:
            minV = minHeap[0]
            num = minV
            for i in range(groupSize):
                if num not in hashMap or hashMap[num] == 0:
                    return False
                hashMap[num] -= 1
                num += 1
                count += 1
            while minHeap and hashMap[minHeap[0]] == 0:
                heapq.heappop(minHeap)

        return True
