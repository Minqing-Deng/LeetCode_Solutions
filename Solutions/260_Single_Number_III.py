from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        # 3: 0011
        # 5: 0101
        # xor: 0110 at least one position is 1

        xor = 0
        for num in nums:
            xor = xor ^ num

        # find the right most different digit:
        whichOne = 1  # 0001
        while not (whichOne & xor):
            whichOne = whichOne << 1

        a, b = 0, 0
        for num in nums:
            if whichOne & num:
                a = a ^ num
            else:
                b = b ^ num

        return [a, b]