from typing import List
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        sorted_list = SortedList()

        for i, num in enumerate(nums):
            # Remove elements outside the indexDiff range
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])

            # Find the position where `num` could be inserted
            pos = sorted_list.bisect_left(num)

            # Check if the closest numbers satisfy the valueDiff condition
            if pos < len(sorted_list) and abs(sorted_list[pos] - num) <= valueDiff:
                return True
            if pos > 0 and abs(sorted_list[pos - 1] - num) <= valueDiff:
                return True

            # Add current number to the sorted list
            sorted_list.add(num)

        return False