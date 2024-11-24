from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # bucket sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count[n] + 1 if n in count else 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)