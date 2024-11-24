from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashMap = {}  # num: index

        for i, n in enumerate(nums):

            if n not in hashMap:
                hashMap[n] = i

            else:
                if i - hashMap[n] <= k:
                    return True

            # for this situation: [1,0,1,1] should return true
            hashMap[n] = i

        return False