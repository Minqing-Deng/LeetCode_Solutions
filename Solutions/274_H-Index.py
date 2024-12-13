from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        # for i, c in enumerate(citations):
        #     if i + 1 >= c:
        #         return c

        h = 0
        for i, citation in enumerate(citations):
            # Check if the current citation count is greater than or equal to the position (1-based)
            if citation >= i + 1:
                h = i + 1
            else:
                break

        return h