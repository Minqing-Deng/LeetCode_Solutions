import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2:
            return []

        # Min-heap to store the pairs along with their sums.
        heap = []
        # Push the first pair (nums1[0], nums2[0]) and advance in nums2.
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)

        result = []
        while heap and len(result) < k:
            current_sum, i, j = heapq.heappop(heap)
            result.append((nums1[i], nums2[j]))

            # If there's a next element in nums2, push the new pair.
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result