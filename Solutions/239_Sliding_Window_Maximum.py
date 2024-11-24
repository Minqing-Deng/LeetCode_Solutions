from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums or k == 0:
            return []

        result = []
        dq = deque()  # Deque to store indices

        for i in range(len(nums)):
            # Remove elements that are out of this window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements that are less than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add the current element's index to the deque
            dq.append(i)

            # Start adding to result once the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])  # The element at the front is the max for the window

        return result