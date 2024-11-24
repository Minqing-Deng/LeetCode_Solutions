from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize the tortoise and hare
        tortoise = nums[0]
        hare = nums[0]

        # Step 2: Move tortoise and hare until they meet in the cycle
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Step 3: Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare