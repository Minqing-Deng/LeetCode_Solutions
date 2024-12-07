from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hashMap = {}  # c: end
        for i, c in enumerate(s):
            hashMap[c] = i

        results = []
        start, end = 0, 0

        for i, c in enumerate(s):
            end = max(end, hashMap[c])
            if i == end:
                results.append(end - start + 1)
                start = i + 1

        return results